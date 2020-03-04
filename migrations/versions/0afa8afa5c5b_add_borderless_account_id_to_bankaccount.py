"""Add borderless_account_id to BankAccount

Revision ID: 0afa8afa5c5b
Revises: d01b87ff85d2
Create Date: 2020-03-04 13:54:43.683627

"""

# revision identifiers, used by Alembic.
revision = '0afa8afa5c5b'
down_revision = 'd01b87ff85d2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bank_account', sa.Column('borderless_account_id', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bank_account', 'borderless_account_id')
    # ### end Alembic commands ###