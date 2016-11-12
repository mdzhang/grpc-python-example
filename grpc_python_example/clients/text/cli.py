"""Module with common db cli commands.

Exposes commands as a click group `basic_cmds`.
"""

import click
from grpc_python_example.clients.text import TextClient

__all__ = ['cli']

_client = TextClient()


@click.command()
def _check_health():
    """Checks client health."""
    click.echo(_client.check_health())


@click.command()
@click.argument('facility_id')
def _get_facility(facility_id):
    """Get a facility by id."""
    click.echo(_client.get_facility(int(facility_id)))


_cmds = {
    'check_health': _check_health,
    'get_facility': _get_facility
}


class _GrpcPythonExampleTextClientCli(click.MultiCommand):
    def list_commands(self, ctx):
        return sorted(list(_cmds.keys()))

    def get_command(self, ctx, name):
        return _cmds[name]


cli = _GrpcPythonExampleTextClientCli(help='Text client commands')
