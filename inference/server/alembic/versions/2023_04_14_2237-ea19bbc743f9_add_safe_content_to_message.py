"""Add safe_content to message

Revision ID: ea19bbc743f9
Revises: b66fd8f9da1f
Create Date: 2023-04-14 22:37:41.373382

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision = "ea19bbc743f9"
down_revision = "b66fd8f9da1f"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("message", sa.Column("safe_content", sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("message", "safe_content")
    # ### end Alembic commands ###