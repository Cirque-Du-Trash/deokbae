"""Initial migration.

Revision ID: caa04e5cd6aa
Revises: 
Create Date: 2024-11-07 18:45:46.044397

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'caa04e5cd6aa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mmrs',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('mmr', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mmrs')
    # ### end Alembic commands ###