import scanpy as sc
import torch


def preprocessing(data):
    """Preprocessing"""
    data.raw = data
    sc.pp.filter_cells(data, min_genes=20)
    sc.pp.filter_genes(data, min_cells=20)
    
    sc.pp.normalize_total(data, target_sum=1e4)
    sc.pp.log1p(data)


def pca_lowrank(data, n_component=50, use_rep=None):
    """PCA (fast way)"""
    data.uns["pca"] = {}
    if use_rep is None:
        x_tensor = torch.tensor(data.X.toarray()) if sp.issparse(data.X) else torch.tensor(data.X)
    else:
        assert use_rep in data.obsm_keys()
        x_tensor = torch.tensor(data.obsm[use_rep])
    u, s, v = torch.pca_lowrank(x_tensor, q=n_component)

    explained_variance_ = s.pow(2) / (data.shape[0] - 1)
    total_var = explained_variance_.sum()
    explained_variance_ratio_ = explained_variance_ / total_var
    data.obsm["X_pca"] = torch.matmul(x_tensor, v).numpy()
    data.uns["pca"]["variance"] = explained_variance_.numpy()
    data.uns["pca"]['variance_ratio'] = explained_variance_ratio_.numpy()