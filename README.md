# grpc_python_example

Demos the following:

* a simple service that can return an `Item` from Postgres database using SQLAlchemy as an ORM, and Alembic for migrations
* the following APIs to access the service:
    * grpc
    * RESTful, [JSON-API compliant](http://jsonapi.org/format/) API using Flask
    * text API with CLI using Click
* example Dockerfile and docker-compose.yml file that dockerizes the service and its apis

## Table of Contents

* [Contributing](docs/CONTRIBUTING.md)
* [Todo](docs/TODO.md)
* [License](docs/LICENSE.md)
