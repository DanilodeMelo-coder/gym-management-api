"""add tabela de vinculacao de alunos e treino

Revision ID: 0d73e22d1296
Revises: 67b5329aa0fc
Create Date: 2026-07-07 10:35:04.714671

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0d73e22d1296'
down_revision: Union[str, Sequence[str], None] = '67b5329aa0fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('AlunoTreinos',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('data', sa.DateTime(), nullable=True),
    sa.Column('treino_id', sa.String(), nullable=True),
    sa.Column('aluno_id', sa.String(), nullable=True),
    sa.Column('observacao', sa.String(), nullable=True),
    sa.Column('ativo', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['aluno_id'], ['Usuarios.id'], ),
    sa.ForeignKeyConstraint(['treino_id'], ['Treinos.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('aluno_id', 'treino_id')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('AlunoTreinos')
