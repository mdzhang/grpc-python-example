"""Module that setups grpc service connectors.

Connectors are used throughout grpc_python_example.clients.http."""
from grpc_python_example.services.stubs import health_pb2, items_pb2
from grpc_python_example.services import GrpcServiceConnector

# pylint: disable=invalid-name
health_conn = GrpcServiceConnector(health_pb2.HealthStub)
items_conn = GrpcServiceConnector(items_pb2.ItemMasterStub)
