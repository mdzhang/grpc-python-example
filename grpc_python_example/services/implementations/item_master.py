import logging
import grpc
from grpc_python_example.services.stubs import items_pb2
from grpc_python_example.services.implementations.database import (
        connection as db, models)

log = logging.getLogger(__name__)


class ItemMasterServicer(items_pb2.ItemMasterServicer):
    """Implements ItemMaster protobuf service interface."""

    def GetItem(self, request, context):
        """Retrieve a item from the database.

        Args:
            request: The request value for the RPC.
            context (grpc.ServicerContext)
        """
        item = db.query(models.Item).get(request.id)

        if item:
            item_pb = items_pb2.Item(**item.to_dict())
            return items_pb2.GetItemResponse(item=item_pb)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Item with id %s not found' % request.id)
            return items_pb2.GetItemResponse()
