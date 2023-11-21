[![python >=3.8.0](https://img.shields.io/badge/python-3.8.0-brightgreen)](https://www.python.org/)
[![Documentation Status](https://readthedocs.org/projects/spatialign/badge/?version=latest)](https://spatialign.readthedocs.io/en/latest/?badge=latest)
[![Downloads](https://static.pepy.tech/badge/spatialign)](https://pepy.tech/project/spatialign)
# spatiAlign: An Unsupervised Contrastive Learning Model for Data Integration of Spatially Resolved Transcriptomics
Integrative analysis of spatially resolved transcriptomics datasets empowers a deeper understanding of complex biological systems. However, integrating multiple tissue sections presents challenges for batch effect removal, particularly when the sections are measured by various technologies or collected at different times. Here, we propose spatiAlign, an unsupervised contrastive learning model that employs the expression of all measured genes and the spatial location of cells, to integrate multiple tissue sections. It enables the joint downstream analysis of multiple datasets not only in low-dimensional embeddings but also in the reconstructed full expression space. In benchmarking analysis, spatiAlign outperforms state-of-the-art methods in learning joint and discriminative representations for tissue sections, each potentially characterized by complex batch effects or distinct biological characteristics. Furthermore, we demonstrate the benefits of spatiAlign for the integrative analysis of time-series brain sections, including spatial clustering, differential expression analysis, and particularly trajectory inference that requires a corrected gene expression matrix.
        
# News  
- [2023.08.13]     
  SpatiAlign is online at [BioRxiv](https://doi.org/10.1101/2023.08.08.552402).        
  doi: [https://doi.org/10.1101/2023.08.08.552402](https://doi.org/10.1101/2023.08.08.552402)       

	
# Citation
If you use `spatiAlign` in your work, please cite the publication as follows:
```
@article {Zhang2023.08.08.552402,
	author = {Chao Zhang and Lin Liu and Ying Zhang and Mei Li and Shuangsang Fang and Qiang Kang and Ao Chen and Xun Xu and Yong Zhang and Yuxiang Li},
	title = {spatiAlign: An Unsupervised Contrastive Learning Model for Data Integration of Spatially Resolved Transcriptomics},
	elocation-id = {2023.08.08.552402},
	year = {2023},
	doi = {10.1101/2023.08.08.552402},
	URL = {https://www.biorxiv.org/content/early/2023/08/15/2023.08.08.552402},
	journal = {bioRxiv}
}
```
                    
        
# Dependences       
[![anndata-0.8.0](https://img.shields.io/badge/anndata-0.8.0-red)](https://pypi.org/project/anndata/#history)
[![scanpy-1.8.2](https://img.shields.io/badge/scanpy-1.8.2-lightgrey)](https://pypi.org/project/scanpy/)
[![torch-1.10.0](https://img.shields.io/badge/torch-1.10.0-brightgreen)](https://pytorch.org/get-started/previous-versions/)
[![torch_geometric-2.0.2](https://img.shields.io/badge/torch_geometric-2.0.2-yellow)](https://pytorch-geometric.readthedocs.io/en/latest/install/installation.html)
[![torch_cluster-1.5.9](https://img.shields.io/badge/torch_cluster-1.5.9-green)](https://data.pyg.org/whl/torch-1.10.0%2Bcu113.html)
[![torch_scatter-2.0.9](https://img.shields.io/badge/torch_scatter-2.0.9-informational)](https://data.pyg.org/whl/torch-1.10.0%2Bcu113.html)
[![torch_sparse-0.6.12](https://img.shields.io/badge/torch_sparse-0.6.12-9cf)](https://data.pyg.org/whl/torch-1.10.0%2Bcu113.html)           



# Install     
- Install through [Pypi](https://pypi.org/project/spatialign/)
```python
pip install spatialign
```

- or git clone
```python
git clone https://github.com/STOmics/Spatialign.git

cd Spatialign

python setup.py install
```

- or docker env
```docker
docker pull zhangchao162/spatialign
```

        
        
# Tutorial
- [Quick Start](https://spatialign.readthedocs.io/en/latest/)
                        

```python
from spatialign import Spatialign

data_lists = $DATA_PATH  # dataset list
model = Spatialign(*data_lists,
                   min_genes=20,
                   min_cells=20,
                   batch_key='batch',
                   is_norm_log=True,
                   is_scale=False,
                   is_hvg=False,
                   is_reduce=False,
                   n_pcs=100,
                   n_hvg=2000,
                   n_neigh=15,
                   is_undirected=True,
                   latent_dims=100,
                   gpu=0,
                   save_path='./output')

model.train(tau1=0.05, tau2=0.01, tau3=0.1)  # training model
model.alignment()  # remove batch effects and align datasets distibution
```
#### ***Note: For more formal parameter descriptions, see the comments of corresponding functions.***           
        
        
# Publicly available datasets            
- Stereo-seq Datasets: mouse olfactory bulb dataset has been deposited into CNGB Sequence Archive (CNSA) of China National GeneBank DataBase (CNGBdb) with accession number CNP001543, and the spatiotemporal dataset of mouse embryonic brain is available at https://db.cngb.org/stomics/mosta.          
- 10x Genomics Visium Dataset: (mouse olfactory bulb) https://www.10xgenomics.com/resources/datasets/adult-mouse-olfactory-bulb-1-standard. And (DLPFC datasets): https://zenodo.org/record/6925603#.YuM5WXZBwuU  
- Slide-seq Datasets: (mouse hippocampus datasets) https://singlecell.broadinstitute.org/single_cell/study/SCP815/highly-sensitive-spatial-transcriptomics-at-near-cellular-resolution-with-slide-seqv2#study-summary, https://singlecell.broadinstitute.org/single_cell/study/SCP354/slide-seq-study#study-summary, and https://singlecell.broadinstitute.org/single_cell/study/SCP948/robust-decomposition-of-cell-type-mixtures-in-spatial-transcriptomics#study-summary, respectively.
        
        
# Disclaimer        
***This is not an official product.***        
        
        
            
        
