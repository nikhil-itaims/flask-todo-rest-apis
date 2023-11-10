""" It has methods for module's CRUD operations.
"""
from app import db
from app.constants import constant
from sqlalchemy import desc, asc

class BaseMethod:
    def __init__(self, model):
        self.model=model

    def save(self, data):
        """ Saves data to the database."""
        try:
            db.session.add(data)
            db.session.commit()
            return constant.STATUS_TRUE, data
        except Exception as err:
            print(err)
            db.session.rollback()
            db.session.close()
            return constant.STATUS_FALSE
        

    def save_all(self, data: list):
        """ Saves data to the database."""
        try:
            db.session.add_all(data)
            db.session.commit()
            return constant.STATUS_TRUE
        except Exception as err:
            print(err)
            db.session.rollback()
            db.session.close()
            return constant.STATUS_FALSE


    def delete(self, data):
        """ Deletes a data from the database """
        try:
            db.session.delete(data)
            db.session.commit()
            return constant.STATUS_TRUE
        except Exception as err:
            db.session.rollback()
            db.session.close()
            return constant.STATUS_FALSE

    def delete_all(self):
        """ Deletes bulk data from the database """
        try:
            self.query.delete()
            db.session.commit()
            return constant.STATUS_TRUE
        except Exception as err:
            db.session.close()
            db.session.rollback()
            return constant.STATUS_FALSE

    def all(self):
        """ Return all of the data in the database """
        query = self.model.query
        count = query.count()
        data = query
        return data, count


    def all_with_operations(self, order_op=constant.ORDER_OP,
                            order_by_column=constant.ORDER_COLUMN,
                            search_by=None):
        "Return all of the data with soring and searching."
        order_op = asc if order_op == 'asc' else desc
        # Filter the deleted data
        query = self.model.query
        count = query.count()
        data = query.order_by(order_op(order_by_column))
        # data = query.all()
        return data, count
        

    def all_with_pagination(self, page, per_page, 
                            order_op=constant.ORDER_OP,
                            order_by_column=constant.ORDER_COLUMN,
                            search_by=None):
        """ Return all of the data in the database """
        order_op = desc if order_op == 'desc' else asc
        # Filter the deleted data
        query = self.model.query
        count = query.count()
        
        query = query.order_by(order_op(order_by_column))
        data = query.paginate(page=page, per_page=per_page)
        return data, count


    def find_by_id(self, id):
        """This function is used to find users by its ID"""
        return self.model.query.filter_by(id=id).first()


    def fetch_all_ids(self) :
        """"This function is used to fetch all the ids 
        of table.
        """
        query = self.model.query.\
            with_entities(self.model.id)
        data = query.all()
        ids = [i.id for i in data ]
        return ids