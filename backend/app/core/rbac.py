from app.db.session import Role

# Permission strings used across API routes
PERMISSIONS = {
    "cluster:read",
    "cluster:write",
    "workload:read",
    "workload:write",
    "incident:read",
    "incident:write",
    "billing:read",
    "billing:write",
    "user:manage",
    "audit:read",
}

ROLE_PERMISSIONS: dict[Role, set[str]] = {
    Role.platform_admin: PERMISSIONS,
    Role.cluster_admin: {
        "cluster:read",
        "cluster:write",
        "workload:read",
        "workload:write",
        "incident:read",
        "incident:write",
    },
    Role.developer: {"cluster:read", "workload:read", "workload:write"},
    Role.sre: {
        "cluster:read",
        "workload:read",
        "workload:write",
        "incident:read",
        "incident:write",
    },
    Role.finops_viewer: {"cluster:read", "billing:read"},
    Role.auditor: {
        "cluster:read",
        "workload:read",
        "incident:read",
        "billing:read",
        "audit:read",
    },
}


def role_has_permission(role: Role, permission: str) -> bool:
    return permission in ROLE_PERMISSIONS.get(role, set())
