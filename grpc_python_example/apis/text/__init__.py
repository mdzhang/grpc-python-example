"""Module with text client for grpc_python_example's grpc server."""

from google.protobuf import text_format
from grpc_python_example.services.stubs import health_pb2, items_pb2
from grpc_python_example.services import GrpcServiceConnector


class TextClient(object):
    """A text client for grpc_python_example's grpc server."""
    def __init__(self):
        self.health_conn = GrpcServiceConnector(health_pb2.HealthStub)
        self.items_master_conn = GrpcServiceConnector(items_pb2.ItemMasterStub)

        self.health_conn.start()
        self.items_master_conn.start()

    def check_health(self):
        """Checks that the text client is connected and that the grpc server
        is available.

        Raises:
            grpc._channel._Rendezvous: When grpc server is down

        Returns:
            str: True or False depending on connection state
        """
        res = self.health_conn.stub.Check(health_pb2.HealthCheckRequest())
        return str(res.status == health_pb2.HealthCheckResponse.SERVING)

    def get_item(self, item_id):
        """Retrieve a item.

        Args:
            item_id (int): id of item to retrieve

        Raises:
            grpc._channel._Rendezvous: When grpc server is down

        Returns:
            str: True or False depending on connection state
        """
        req = items_pb2.GetItemRequest(id=item_id)
        res = self.items_master_conn.stub.GetItem(req)
        return text_format.MessageToString(res)
