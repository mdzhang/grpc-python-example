"""create and seed item table

Revision ID: 86998e2c2489
Revises:
Create Date: 2016-11-13 23:15:07.925884

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table


# revision identifiers, used by Alembic.
revision = '86998e2c2489'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'items',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
    )

    items_table = table(
        'items',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
    )

    op.bulk_insert(items_table,
        [
            {
                'id': 1,
                'name': 'Green Eggs'
            },
            {
                'id': 2,
                'name': 'Ham'
            }
        ]
    )

def downgrade():
    op.drop_table('items')
