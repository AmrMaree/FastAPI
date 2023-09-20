"""add content column to posts table

Revision ID: 9e91a4af7028
Revises: ec39b0fdd4d5
Create Date: 2023-09-20 20:03:30.008178

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9e91a4af7028'
down_revision: Union[str, None] = 'ec39b0fdd4d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
