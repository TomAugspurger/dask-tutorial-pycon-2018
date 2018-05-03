def make_cluster():
    try:
        from dask_kubernetes import KubeCluster
        cluster = KubeCluster()
    except ImportError:
        from distributed.deploy.local import LocalCluster
        cluster = LocalCluster()
    return cluster
