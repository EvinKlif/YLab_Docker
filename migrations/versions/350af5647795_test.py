"""Test

Revision ID: 350af5647795
Revises: 
Create Date: 2023-07-30 23:56:44.074848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '350af5647795'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('menus',
    sa.Column('target_menus_id', sa.UUID(), nullable=False),
    sa.Column('target_menus_title', sa.String(length=50), nullable=True),
    sa.Column('target_menus_description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('target_menus_id'),
    sa.UniqueConstraint('target_menus_title')
    )
    op.create_table('submenus',
    sa.Column('target_submenus_id', sa.UUID(), nullable=False),
    sa.Column('target_submenus_title', sa.String(length=50), nullable=True),
    sa.Column('target_submenus_description', sa.Text(), nullable=True),
    sa.Column('menus_id', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['menus_id'], ['menus.target_menus_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('target_submenus_id'),
    sa.UniqueConstraint('target_submenus_title')
    )
    op.create_table('dishes',
    sa.Column('target_dishes_id', sa.UUID(), nullable=False),
    sa.Column('target_dishes_title', sa.String(length=50), nullable=True),
    sa.Column('target_dishes_description', sa.Text(), nullable=True),
    sa.Column('target_dishes_price', sa.String(length=50), nullable=True),
    sa.Column('submenus_id', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['submenus_id'], ['submenus.target_submenus_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('target_dishes_id'),
    sa.UniqueConstraint('target_dishes_title')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dishes')
    op.drop_table('submenus')
    op.drop_table('menus')
    # ### end Alembic commands ###