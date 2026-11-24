"""Initial CEO users, employees, and audit logs."""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
revision="0001_initial"
down_revision=None
branch_labels=None
depends_on=None
def upgrade()->None:
    op.create_table("ceo_users",sa.Column("id",postgresql.UUID(as_uuid=True),primary_key=True),sa.Column("email",sa.String(320),nullable=False),sa.Column("password_hash",sa.String(512),nullable=False),sa.Column("is_active",sa.Boolean(),nullable=False,server_default=sa.true()),sa.Column("created_at",sa.DateTime(timezone=True),server_default=sa.func.now(),nullable=False))
    op.create_index("ix_ceo_users_email","ceo_users",["email"],unique=True)
    op.create_table("employees",sa.Column("id",postgresql.UUID(as_uuid=True),primary_key=True),sa.Column("slug",sa.String(40),nullable=False),sa.Column("display_name",sa.String(80),nullable=False),sa.Column("role",sa.String(100),nullable=False),sa.Column("department",sa.String(80),nullable=False),sa.Column("status",sa.String(24),nullable=False,server_default="inactive"),sa.Column("created_at",sa.DateTime(timezone=True),server_default=sa.func.now(),nullable=False),sa.Column("updated_at",sa.DateTime(timezone=True),server_default=sa.func.now(),nullable=False))
    op.create_index("ix_employees_slug","employees",["slug"],unique=True)
    op.create_table("audit_logs",sa.Column("id",postgresql.UUID(as_uuid=True),primary_key=True),sa.Column("actor_type",sa.String(24),nullable=False),sa.Column("actor_id",sa.String(80),nullable=False),sa.Column("action",sa.String(120),nullable=False),sa.Column("resource_type",sa.String(80),nullable=False),sa.Column("resource_id",sa.String(80)),sa.Column("request_id",sa.String(80)),sa.Column("details",sa.JSON(),nullable=False),sa.Column("created_at",sa.DateTime(timezone=True),server_default=sa.func.now(),nullable=False))
    op.create_index("ix_audit_logs_actor_id","audit_logs",["actor_id"])
    op.create_index("ix_audit_logs_action","audit_logs",["action"])
    op.create_index("ix_audit_logs_request_id","audit_logs",["request_id"])
def downgrade()->None:
    op.drop_index("ix_audit_logs_request_id",table_name="audit_logs")
    op.drop_index("ix_audit_logs_action",table_name="audit_logs")
    op.drop_index("ix_audit_logs_actor_id",table_name="audit_logs")
    op.drop_table("audit_logs")
    op.drop_index("ix_employees_slug",table_name="employees")
    op.drop_table("employees")
    op.drop_index("ix_ceo_users_email",table_name="ceo_users")
    op.drop_table("ceo_users")
