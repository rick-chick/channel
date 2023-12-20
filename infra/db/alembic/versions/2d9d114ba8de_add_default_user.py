"""add default user

Revision ID: 2d9d114ba8de
Revises: 82555ec1294d
Create Date: 2023-12-14 20:20:06.252340

"""
from typing import Sequence, Union
from sqlalchemy.sql import table, column
from sqlalchemy import String, DateTime

from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision: str = '2d9d114ba8de'
down_revision: Union[str, None] = '82555ec1294d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    user_table = table(
        "users",
        column("id", String),
        column("email", String),
        column("password_hash", String),
        column("created_by", String),
        column("updated_by", String),
        column("created_at", DateTime),
        column("updated_at", DateTime),
    )

    conn = op.get_bind()
    conn.execute(
        user_table.insert()
        .values(
            id="0e83d5fd-624e-4e58-9e80-273895b4850f",
            email="test@admin.com",
            password_hash="$2b$12$wWo0b7DsIoM4QhWd0iJfPeko4EMg9TB2YFLISdVkPV7KE5YxDo7Nq",
            created_by="system",
            updated_by="system",
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
    )


def downgrade() -> None:
    user_table = table(
        "users",
        column("id", String),
    )

    conn = op.get_bind()
    conn.execute(
        user_table.delete()
        .where(
            user_table.c.id == "0e83d5fd-624e-4e58-9e80-273895b4850f",
        )
    )
