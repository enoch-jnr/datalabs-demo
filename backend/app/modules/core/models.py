import uuid

from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.core.mixins import ActiveMixin, TimestampMixin, UUIDMixin
from app.modules.core.enums import PermissionAction, RoleScope


class User(Base, UUIDMixin, TimestampMixin, ActiveMixin):
    __tablename__ = "users"
    __table_args__ = {"schema": "core"}

    email = Column(String(255), unique=True, nullable=False, index=True)
    username = Column(String(100), unique=True, nullable=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    password_hash = Column(String(255), nullable=False)

    is_verified = Column(Boolean, default=False, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    last_login_at = Column(DateTime(timezone=True), nullable=True)

    oauth_provider = Column(String(50), nullable=True)
    oauth_subject = Column(String(255), nullable=True)

    user_roles = relationship("UserRole", back_populates="user", cascade="all, delete-orphan")
    workspaces = relationship("Workspace", back_populates="owner")


class Role(Base, UUIDMixin, TimestampMixin, ActiveMixin):
    __tablename__ = "roles"
    __table_args__ = {"schema": "core"}

    name = Column(String(100), unique=True, nullable=False)
    scope = Column(Enum(RoleScope), nullable=False, default=RoleScope.PROJECT)
    description = Column(String(500), nullable=True)
    is_system_role = Column(Boolean, default=False, nullable=False)

    role_permissions = relationship("RolePermission", back_populates="role", cascade="all, delete-orphan")
    user_roles = relationship("UserRole", back_populates="role", cascade="all, delete-orphan")


class Permission(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "permissions"
    __table_args__ = (
        UniqueConstraint("resource", "action", name="uq_permission_resource_action"),
        {"schema": "core"},
    )

    resource = Column(String(100), nullable=False, index=True)
    action = Column(Enum(PermissionAction), nullable=False)
    description = Column(String(500), nullable=True)

    role_permissions = relationship("RolePermission", back_populates="permission", cascade="all, delete-orphan")


class RolePermission(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "role_permissions"
    __table_args__ = (
        UniqueConstraint("role_id", "permission_id", name="uq_role_permission"),
        {"schema": "core"},
    )

    role_id = Column(UUID(as_uuid=True), ForeignKey("core.roles.id", ondelete="CASCADE"), nullable=False)
    permission_id = Column(UUID(as_uuid=True), ForeignKey("core.permissions.id", ondelete="CASCADE"), nullable=False)

    role = relationship("Role", back_populates="role_permissions")
    permission = relationship("Permission", back_populates="role_permissions")


class UserRole(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "user_roles"
    __table_args__ = (
        UniqueConstraint("user_id", "role_id", "scope_id", name="uq_user_role_scope"),
        {"schema": "core"},
    )

    user_id = Column(UUID(as_uuid=True), ForeignKey("core.users.id", ondelete="CASCADE"), nullable=False, index=True)
    role_id = Column(UUID(as_uuid=True), ForeignKey("core.roles.id", ondelete="CASCADE"), nullable=False, index=True)

    # generic pointer to whichever entity this role grants access to
    # (an enterprise id, a workspace id, a project id, etc.) — kept as a
    # bare UUID rather than an FK since it can point at several tables.
    scope_id = Column(UUID(as_uuid=True), nullable=True)

    user = relationship("User", back_populates="user_roles")
    role = relationship("Role", back_populates="user_roles")
