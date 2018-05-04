def make_cluster(**kwargs):
    try:
        from dask_kubernetes import KubeCluster
        kwargs.setdefault('n_workers', 10)
        cluster = KubeCluster(**kwargs)
    except ImportError:
        from distributed.deploy.local import LocalCluster
        cluster = LocalCluster()
    return cluster
