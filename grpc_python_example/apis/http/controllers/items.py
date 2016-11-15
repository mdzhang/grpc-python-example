"""Flask blueprint for /items* endpoint.

Exposes the blueprint as a module-level variable named `main`.
"""
from flask import Blueprint
from flask_ripozo import FlaskDispatcher
from ripozo import restmixins
from ripozo.manager_base import BaseManager
from ripozo.adapters import JSONAPIAdapter
from ripozo.resources.fields.common import StringField, IntegerField
from grpc_python_example.services.stubs import items_pb2
from grpc_python_example.apis.http.services import items_conn

# pylint: disable=invalid-name
items = Blueprint('items', __name__)


class ItemManager(BaseManager):
    """Manager that interops between ripozo and grpc.

    Provides convience functions primarily for basic CRUD.
    """
    fields = ('id', 'name',)
    field_validators = [
        IntegerField('id', required=True),
        StringField('name', required=True),
    ]

    def create(self, values, *args, **kwargs):
        raise NotImplementedError()

    def delete(self, lookup_keys, *args, **kwargs):
        raise NotImplementedError()

    def retrieve(self, lookup_keys, *args, **kwargs):
        """Retrieve a single item and nothing more as a dictionary.

        Args:
            lookup_keys (dict): Taken from url_params on flask request. Used to
                lookup a item and its associated values.

        Returns:
            dict or None: Properties of the retrieved item or None if no
                such item found.
        """
        resp = items_conn.stub.GetItem(
            items_pb2.GetItemRequest(id=lookup_keys['id']))
        item = resp.item

        if item:
            return dict(id=item.id, name=item.name)

    def retrieve_list(self, filters, *args, **kwargs):
        raise NotImplementedError()

    def update(self, lookup_keys, updates, *args, **kwargs):
        raise NotImplementedError()


class ItemResource(restmixins.Retrieve):
    """Standard ripozo resource that can be used by ripozo adapters. Handles
    requests and constructs resources to return as a request.
    """
    manager = ItemManager()
    pks = 'id',
    resource_name = 'items'


# register resources and valid response types
_dispatcher = FlaskDispatcher(items)
_dispatcher.register_adapters(JSONAPIAdapter)
_dispatcher.register_resources(ItemResource)
