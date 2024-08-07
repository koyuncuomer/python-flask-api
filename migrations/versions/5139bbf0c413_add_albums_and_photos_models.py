"""Add albums and photos models

Revision ID: 5139bbf0c413
Revises: 95a7c96abaf8
Create Date: 2024-06-27 12:29:15.568240

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5139bbf0c413'
down_revision = '95a7c96abaf8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('album',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('photo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('album_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('url', sa.String(length=200), nullable=True),
    sa.Column('thumbnail_url', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['album_id'], ['album.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('photo')
    op.drop_table('album')
    # ### end Alembic commands ###
