"""add last few columns to post table

Revision ID: 0e618bb31b7d
Revises: 9ff8cfade1bd
Create Date: 2021-11-30 11:09:18.769699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e618bb31b7d'
down_revision = '9ff8cfade1bd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('published',sa.Boolean,nullable=False,server_default='TRUE'))
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')))
    pass


def downgrade():
    pass
