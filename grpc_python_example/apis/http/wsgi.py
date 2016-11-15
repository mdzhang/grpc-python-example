"""WSGI config for grpc_python_example.apis.http.

Exposes the WSGI callable as a module-level variable named `app`.
"""
import os
from grpc_python_example.apis.http import create_app

# pylint: disable=invalid-name
env = os.environ.get('ENV', 'development')
app = create_app('grpc_python_example.apis.http.settings.%sConfig' % env.capitalize())


if __name__ == '__main__':
    app.run()
