#!/usr/bin/env bash
set -euo pipefail

echo 'Creating database...'
python -m grpc_python_example.database.cli create

echo 'Running database migrations...'
alembic upgrade head

echo 'Starting grpc server...'
make run-server
