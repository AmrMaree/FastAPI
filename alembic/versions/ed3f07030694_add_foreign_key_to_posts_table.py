"""add foreign key to posts table

Revision ID: ed3f07030694
Revises: d4ee8fa5d04d
Create Date: 2023-09-21 00:21:03.771127

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ed3f07030694'
down_revision: Union[str, None] = 'd4ee8fa5d04d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fkey', source_table="posts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fkeys', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
