import threading
import grpc
from grpc_python_example.services.stubs import health_pb2


class HealthServicer(health_pb2.HealthServicer):
    """Implements Health protobuf service interface.

    Notes:
        Taken from https://github.com/grpc/grpc/tree/master/src/python/grpcio_health_checking
        SHA: d953959e2bafd645b6ed674861a310daba5f80ae
        because of slow package setup speed
    """

    def __init__(self):
        self._server_status_lock = threading.Lock()
        self._server_status = {}

    def Check(self, request, context):
        with self._server_status_lock:
            status = self._server_status.get(request.service)
            if status is None:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return health_pb2.HealthCheckResponse()
            else:
                return health_pb2.HealthCheckResponse(status=status)

    def set(self, service, status):
        """Sets the status of a service.
        Args:
            service: string, the name of the service.
                NOTE, '' must be set.
            status: HealthCheckResponse.status enum value indicating
                the status of the service
        """
        with self._server_status_lock:
            self._server_status[service] = status
