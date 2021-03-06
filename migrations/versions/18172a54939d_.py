"""empty message

Revision ID: 18172a54939d
Revises: a56f61dee447
Create Date: 2019-03-25 07:44:07.042570

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '18172a54939d'
down_revision = 'a56f61dee447'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('account', sa.Column('role', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('account', 'role')
    # ### end Alembic commands ###
