#!/usr/bin/env bash
set -euo pipefail

echo 'Creating database...'
python -m grpc_python_example.services.implementations.database.cli create

echo 'Running database migrations...'
alembic upgrade head

echo 'Starting grpc api...'
make run-grpc-api
