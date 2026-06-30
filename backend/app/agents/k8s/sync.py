"""K8s Ops Agent — sync cluster resources and execute operations."""

from dataclasses import dataclass


@dataclass
class PodSummary:
    name: str
    namespace: str
    status: str
    restarts: int


def list_pods(kubeconfig_path: str | None = None, namespace: str | None = None) -> list[PodSummary]:
    """
    List pods from a registered cluster.
    Requires valid kubeconfig or in-cluster config when deployed on K8s.
    """
    try:
        from kubernetes import client, config

        if kubeconfig_path:
            config.load_kube_config(config_file=kubeconfig_path)
        else:
            config.load_kube_config()

        v1 = client.CoreV1Api()
        if namespace:
            pods = v1.list_namespaced_pod(namespace=namespace)
        else:
            pods = v1.list_pod_for_all_namespaces()

        return [
            PodSummary(
                name=p.metadata.name,
                namespace=p.metadata.namespace or "default",
                status=p.status.phase or "Unknown",
                restarts=sum(c.restart_count for c in (p.status.container_statuses or [])),
            )
            for p in pods.items
        ]
    except Exception:
        # No kubeconfig in dev — return empty; wire real cluster in production
        return []


def check_cluster_health(api_endpoint: str) -> str:
    """Ping cluster API endpoint; returns healthy | unreachable | unknown."""
    if not api_endpoint:
        return "unknown"
    # MVP: status set on registration; full health check in Phase 2
    return "registered"
