"""empty message

Revision ID: aeb0000a2c30
Revises: f796b4ae58c4
Create Date: 2019-10-04 15:31:09.163223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aeb0000a2c30'
down_revision = 'f796b4ae58c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('city_venue_address_link',
    sa.Column('city_id', sa.Integer(), nullable=False),
    sa.Column('venue_address_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['city_id'], ['cities.id'], ),
    sa.ForeignKeyConstraint(['venue_address_id'], ['venue_address.id'], ),
    sa.PrimaryKeyConstraint('city_id', 'venue_address_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('city_venue_address_link')
    # ### end Alembic commands ###