"""Module that manages database connection."""
import os
from sqlalchemy_wrapper import SQLAlchemy

# pylint: disable=invalid-name
# Connect to the database
connection = SQLAlchemy(os.environ['DATABASE_URL'])
