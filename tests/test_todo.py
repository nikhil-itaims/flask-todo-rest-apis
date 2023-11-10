import unittest
from flask import jsonify
from app import app

class TestCRUDAPIs(unittest.TestCase):

    def test_create_todo(self):
        # Create a new todo item
        response = app.test_client().post("/todo", json={"todo_name": "My new todo item"})

        # Check the response status code
        self.assertEqual(response.status_code, 201)

        # Check the response data
        data = jsonify(response.json)
        self.assertEqual(data['data']["todo_name"], "My new todo item")

    def test_get_all_todos(self):
        # Create a few todo items
        app.test_client().post("api/v1/todo", json={"todo_name": "My first todo item"})
        app.test_client().post("api/v1/todo", json={"todo_name": "My second todo item"})

        # Get all todo items
        response = app.test_client().get("api/v1/todo")

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check the response data
        data = jsonify(response.json)
        self.assertEqual(len(data), 2)
        self.assertIn("My first todo item", data['data'])
        self.assertIn("My second todo item", data['data'])

    def test_get_single_todo(self):
        # Create a new todo item
        response = app.test_client().post("api/v1/todo", json={"todo_name": "My new todo item"})

        # Get the todo item by ID
        todo_id = response.json["id"]
        response = app.test_client().get("api/v1/todo/{}".format(todo_id))

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check the response data
        data = jsonify(response.json)
        self.assertEqual(data["todo_name"], "My new todo item")

    def test_update_todo(self):
        # Create a new todo item
        response = app.test_client().post("/todo", json={"todo_name": "My new todo item"})

        # Get the todo item by ID
        todo_id = response.json["id"]

        # Update the todo item
        response = app.test_client().put("/todo/{}".format(todo_id), json={"todo_name": "My updated todo item"})

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check the response data
        data = jsonify(response.json)
        self.assertEqual(data["todo_name"], "My updated todo item")

    def test_delete_todo(self):
        # Create a new todo item
        response = app.test_client().post("/todo", json={"todo_name": "My new todo item"})

        # Get the todo item by ID
        todo_id = response.json["id"]

        # Delete the todo item
        response = app.test_client().delete("/todo/{}".format(todo_id))

        # Check the response status code
        self.assertEqual(response.status_code, 204)

        # Make sure the todo item is gone
        response = app.test_client().get("/todo/{}".format(todo_id))

        # Check the response status code
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()