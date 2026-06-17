"""add usuario_id fk to tarefas

Revision ID: 1077d5c5040e
Revises: 18022e0bd787
Create Date: 2026-06-17 12:25:45.861315

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1077d5c5040e'
down_revision: Union[str, Sequence[str], None] = '18022e0bd787'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('tarefas') as batch_op:
        batch_op.add_column(sa.Column('usuario_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(
            'fk_tarefas_usuario_id', 'usuarios', ['usuario_id'], ['id']
        )

def downgrade() -> None:
    with op.batch_alter_table('tarefas') as batch_op:
        batch_op.drop_constraint('fk_tarefas_usuario_id', type_='foreignkey')
        batch_op.drop_column('usuario_id')
