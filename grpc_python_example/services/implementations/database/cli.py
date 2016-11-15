"""Module with common database commands.

Exposes commands as a click multicommand `cli`.
"""

import click
from sqlalchemy_utils import database_exists, create_database
from grpc_python_example.services.implementations.database import (
        connection as db)


@click.command()
def _create():
    """Create database."""
    if not database_exists(db.engine.url):
        create_database(db.engine.url)


@click.command()
def _drop_tables():
    """Drop all database tables."""
    db.drop_all()


@click.command()
def _create_tables():
    """Create all database tables."""
    db.create_all()


_cmds = {
    'create': _create,
    'drop_tables': _drop_tables,
    'create_tables': _create_tables,
}


class _GrpcPythonExampleDatabaseCli(click.MultiCommand):
    def list_commands(self, ctx):
        return sorted(list(_cmds.keys()))

    def get_command(self, ctx, name):
        return _cmds[name]


cli = _GrpcPythonExampleDatabaseCli(help='Database commands')


if __name__ == '__main__':
    cli()
