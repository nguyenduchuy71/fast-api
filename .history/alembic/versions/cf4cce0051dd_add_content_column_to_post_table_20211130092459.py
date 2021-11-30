"""add content column to post table

Revision ID: cf4cce0051dd
Revises: 9d9c2a704df4
Create Date: 2021-11-30 09:23:56.447519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf4cce0051dd'
down_revision = '9d9c2a704df4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String, nullable=False))
    pass


def downgrade():
    pass
