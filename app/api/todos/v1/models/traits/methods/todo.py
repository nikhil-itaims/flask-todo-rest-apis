""" It has methods for Todo's CRUD operations.
"""
from operator import or_
from sqlalchemy import desc, asc
from app.constants import constant
from app.api.todos.v1.models.todo import Todo


class TodoMethod(Todo):
    def __init__(self):
        pass

    def find_by_id(self, id):
        """This function is used to find todo by id"""
        return self.query.filter_by(id=id).first()

    def find_by_name(self, name):
        """This function is used to find todo by name"""
        return self.query.filter_by(todo_name=name).first()
    
    
    def fetch_all(self):
        """
        Fetch all the todo's list to download for the csv file.
        """
        return self.query.all()
        
        
    def fetch_list(self, order_op, order_by_column,
                    search_by=constant.STATUS_NULL, filter_by=constant.STATUS_ZERO,
                    page=constant.STATUS_NULL, per_page=constant.STATUS_NULL):
        
        """This API isused to get the listing of todo in the admin panel.
            Can apply the pagination and also can search the values from the data.
        Args:
            page (int): The number of the page.
            per_page (int): Limit of the data which you want to show in the listing.
            order_op (str): The order of data to show in the listing (asc or desc).
            order_by_column (str): The name of column which according to order the data.
            search_by (str): The sub string to search from the data.
            filter_by (int): It contains the any value from this - [0,1,2].
                            according to number you can filter the data and get the queries list.
                            0 = all
        Returns:
            list: list of the data
            int: count of the total data
        """
        order_op = desc if order_op == 'desc' else asc
        # query_data = self.query.filter_by(created_at=None)
        query_data = self.query

        # Search the string from table
        if search_by:
            search_by = "%{}%".format(search_by)
            query_data = query_data.filter(Todo.todo_name.like(search_by))
       
        query_data = query_data.order_by(order_op(order_by_column))
        count = query_data.count()
        if not per_page:
            data = query_data
        else:
            data = query_data.paginate(page=page, per_page=per_page)
            data = data.items
        return data, count
    
    
    def fetch_all_ids(self) :
        """"This function is used to fetch all the ids 
        of table.
        """
        query = Todo.query.all().\
            with_entities(Todo.id, Todo.todo_name)
        data = query.all()
        ids = [i.id for i in data ]
        return ids, data
