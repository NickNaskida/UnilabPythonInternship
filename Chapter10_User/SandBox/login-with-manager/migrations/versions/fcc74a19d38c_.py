"""empty message

Revision ID: fcc74a19d38c
Revises: 39bb7ef28bd5
Create Date: 2021-04-21 20:12:04.187668

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fcc74a19d38c'
down_revision = '39bb7ef28bd5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('randoms', schema=None) as batch_op:
        batch_op.drop_column('param3')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('randoms', schema=None) as batch_op:
        batch_op.add_column(sa.Column('param3', sa.VARCHAR(), nullable=True))

    # ### end Alembic commands ###