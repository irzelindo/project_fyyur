"""empty message

Revision ID: b1e88e77fa82
Revises: 62cf8dacabb2
Create Date: 2019-10-10 17:33:45.710295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1e88e77fa82'
down_revision = '62cf8dacabb2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('venue_address_venue_id_fkey', 'venue_address', type_='foreignkey')
    op.drop_column('venue_address', 'venue_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue_address', sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('venue_address_venue_id_fkey', 'venue_address', 'venues', ['venue_id'], ['id'])
    # ### end Alembic commands ###
