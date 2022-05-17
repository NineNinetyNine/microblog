"""followers

Revision ID: 28c65d35d40e
Revises: 4f4ade234809
Create Date: 2022-05-17 12:46:51.293506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28c65d35d40e'
down_revision = '4f4ade234809'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
