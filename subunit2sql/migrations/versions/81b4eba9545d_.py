"""empty message

Revision ID: 81b4eba9545d
Revises: 10a2b6d4b06e
Create Date: 2016-05-13 15:41:27.488747

"""

# revision identifiers, used by Alembic.
revision = '81b4eba9545d'
down_revision = '10a2b6d4b06e'

from alembic import context
from alembic import op

import sqlalchemy as sa


def upgrade():
    migration_context = context.get_context()

    if migration_context.dialect.name != 'mysql':
        return

    op.add_column('runs', sa.Column('my_metadata', sa.JSON()))
    op.add_column('tests', sa.Column('my_metadata', sa.JSON()))
    op.add_column('test_runs', sa.Column('my_metadata', sa.JSON()))
    op.drop_table('test_run_metadata')
    op.drop_table('test_metadata')
    op.drop_table('run_metadata')


def downgrade():
    pass
