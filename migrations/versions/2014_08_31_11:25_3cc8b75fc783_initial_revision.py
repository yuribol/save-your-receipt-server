"""Initial revision

Revision ID: 3cc8b75fc783
Revises: None
Create Date: 2014-08-31 11:25:30.835151

"""

# revision identifiers, used by Alembic.
revision = '3cc8b75fc783'
down_revision = None
import datetime

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(50), nullable=False),
        sa.Column("salt", sa.String(20), nullable=False),
        sa.Column("password", sa.String(50), nullable=False),
        sa.Column("created", sa.DateTime(), default=datetime.datetime.utcnow()),
        sa.Column("status", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        "store_chain",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("created", sa.DateTime(), default=datetime.datetime.utcnow()),
        sa.Column("status", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        "store",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("store_chain_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("created", sa.DateTime(), default=datetime.datetime.utcnow()),
        sa.Column("status", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['store_chain_id'], ['store_chain.id'], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        "store_details",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("store_id", sa.Integer(), nullable=False),
        sa.Column("address", sa.String(200), nullable=False),
        sa.Column("city", sa.String(30), nullable=False),
        sa.Column("province", sa.String(20), nullable=False),
        sa.Column("country", sa.String(30), nullable=False),
        sa.Column("postal_code", sa.String(20), nullable=False),
        sa.Column("phone", sa.String(50), nullable=False),
        sa.Column("website", sa.String(200), nullable=False),
        sa.Column("contact_email", sa.String(200), nullable=False),
        sa.Column("created", sa.DateTime(), default=datetime.datetime.utcnow()),
        sa.ForeignKeyConstraint(['store_id'], ['store.id'], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        "budget",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("limit", sa.Float(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        "budget_user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("budget_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(['budget_id'], ['budget.id'], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        "receipt",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("store_id", sa.Integer(), nullable=False),
        sa.Column("receipt_date", sa.DateTime(), default=datetime.datetime.utcnow()),
        sa.Column("receipt_amout", sa.Float(), nullable=False),
        sa.Column("created", sa.DateTime(), default=datetime.datetime.utcnow()),
        sa.Column("status", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(['store_id'], ['store.id'], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table("receipt")
    op.drop_table("budget_user")
    op.drop_table("budget")
    op.drop_table("store_details")
    op.drop_table("store")
    op.drop_table("store_chain")
    op.drop_table("user")
    pass
