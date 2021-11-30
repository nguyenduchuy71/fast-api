"""create posts table

Revision ID: 9d9c2a704df4
Revises: 
Create Date: 2021-11-30 09:14:50.013539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d9c2a704df4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,primary_key=True))
    pass

def downgrade():
    pass
