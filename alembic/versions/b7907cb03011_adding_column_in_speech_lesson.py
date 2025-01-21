"""adding column in speech_lesson

Revision ID: b7907cb03011
Revises: 
Create Date: 2025-01-21 15:55:34.198863

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b7907cb03011'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("speech_lessons",sa.Column('Type', sa.VARCHAR(250), nullable=True))


def downgrade() -> None:
    op.drop_column("speech_lessons", "Type")
