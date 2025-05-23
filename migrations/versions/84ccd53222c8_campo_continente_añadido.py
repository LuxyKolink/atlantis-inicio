"""Campo continente añadido

Revision ID: 84ccd53222c8
Revises: 4eb4a4d67e54
Create Date: 2025-05-12 15:59:09.532525

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '84ccd53222c8'
down_revision: Union[str, None] = '4eb4a4d67e54'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('paises', sa.Column('continente', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.create_index(op.f('ix_paises_continente'), 'paises', ['continente'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_paises_continente'), table_name='paises')
    op.drop_column('paises', 'continente')
    # ### end Alembic commands ###
