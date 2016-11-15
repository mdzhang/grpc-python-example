"""Module with all models used by grpc_python_example."""
from sqlalchemy.inspection import inspect as _inspect
from grpc_python_example.services.implementations.database import (
        connection as db)


__all__ = ['Item']


class _BaseMixin(object):
    """Encapsulating shared functionality of grpc_python_example models."""
    id = db.Column(db.Integer, primary_key=True)

    def to_dict(self):
        """Returns model as dict of properties.

        Note:
            Removes SQLAlchemy fields included in self.__dict__
        """
        column_names = _inspect(self.__class__).columns.keys()
        return {k: self.__dict__[k] for k in column_names}


class Item(_BaseMixin, db.Model):
    """Represents an item.

    Attributes:
        id (int)
        name (str): name of item
    """
    __tablename__ = 'items'
    name = db.Column(db.String)

    def __repr__(self):
        return '<Item(id=%s, code=%s, name=%s)>' % (self.id, self.name)
