"""Module with common db cli commands.

Exposes commands as a click group `basic_cmds`.
"""

import click
from grpc_python_example.apis.text import TextClient

__all__ = ['cli']

_client = TextClient()


@click.command()
def _check_health():
    """Checks client health."""
    click.echo(_client.check_health())


@click.command()
@click.argument('item_id')
def _get_item(item_id):
    """Get an item by id."""
    click.echo(_client.get_item(int(item_id)))


_cmds = {
    'check_health': _check_health,
    'get_item': _get_item
}


class _GrpcPythonExampleTextClientCli(click.MultiCommand):
    def list_commands(self, ctx):
        return sorted(list(_cmds.keys()))

    def get_command(self, ctx, name):
        return _cmds[name]


cli = _GrpcPythonExampleTextClientCli(help='Text client commands')
