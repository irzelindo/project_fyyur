"""empty message

Revision ID: eb03ad4dfbf7
Revises: 5cee3273d365
Create Date: 2019-10-04 13:49:50.454415

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb03ad4dfbf7'
down_revision = '5cee3273d365'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('venue_address_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['venue_address_id'], ['venue_address.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cities')
    # ### end Alembic commands ###
