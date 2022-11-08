"""empty message

Revision ID: 6086df33eb3e
Revises: 5cbcc87798ef
Create Date: 2022-11-08 07:00:36.554432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6086df33eb3e'
down_revision = '5cbcc87798ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('author', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'author')
    # ### end Alembic commands ###
