"""Module with exceptions that grpc_python_example.clients.http explicitly uses."""
from ripozo.exceptions import RestException


class GrpcServiceNotConnectedException(RestException):
    """Raised when trying to call methods on a grpc service stub
    that is not connected on either the HTTP client or grpc server side.
    """
    def __init__(self, message=None, status_code='500', *args, **kwargs):
        super(GrpcServiceNotConnectedException, self).__init__(message,
                                                               *args,
                                                               **kwargs)
        self.status_code = status_code


class UnauthorizedException(RestException):
    """Raised when authorizing a request fails."""
    def __init__(self, message=None, status_code='401', *args, **kwargs):
        super(UnauthorizedException, self).__init__(message, *args, **kwargs)
        self.status_code = status_code


class NotFoundException(RestException):
    """Raised when a requested resource does not exist."""
    def __init__(self, message=None, status_code='404', *args, **kwargs):
        super(NotFoundException, self).__init__(message, *args, **kwargs)
        self.status_code = status_code


class InternalServerException(RestException):
    """Raised when any unhandled exception arises."""
    def __init__(self, message=None, status_code='500', *args, **kwargs):
        super(InternalServerException, self).__init__(message, *args, **kwargs)
        self.status_code = status_code
