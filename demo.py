#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/12/23 11:29 AM
# @Author  : zhangchao
# @File    : demo.py
# @Email   : zhangchao5@genomics.cn
import os
import sys
import warnings
import argparse
from typing import Union

from spatialign import Spatialign

sys.path.append(os.getcwd())
warnings.filterwarnings("ignore")
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="spatialign Running...")
    # init parameters
    parser.add_argument("--data_path", type=Union[list, str], help="Input dataset path")
    parser.add_argument("--min_genes", default=20, type=int,
                        help="Minimum number of genes expressed required for a cell to pass filtering, default 20.")
    parser.add_argument("--min_cells", default=20, type=int,
                        help="Minimum number of cells expressed required for a gene to pass filtering, default 20.")
    parser.add_argument("--batch_key", default="batch", type=str,
                        help="The batch annotation to :attr:`obs` using this key, default, 'batch'.")
    parser.add_argument("--is_norm_log", default=True, type=bool,
                        help="Whether to perform 'sc.pp.normalize_total' and 'sc.pp.log1p' processing, default, True.")
    parser.add_argument("--is_scale", default=False, type=bool,
                        help="Whether to perform 'sc.pp.scale' processing, default, False.")
    parser.add_argument("--is_hvg", default=False, type=bool,
                        help="Whether to perform 'sc.pp.highly_variable_genes' processing, default, False.")
    parser.add_argument("--is_reduce", default=False, type=bool,
                        help="Whether to perform PCA reduce dimensional processing, default, False.")
    parser.add_argument("--n_pcs", default=100, type=int,
                        help="PCA dimension reduction parameter, valid when 'is_reduce' is True, default, 100.")
    parser.add_argument("--n_hvg", default=2000, type=int,
                        help="'sc.pp.highly_variable_genes' parameter, valid when 'is_reduce' is True, default, 2000.")
    parser.add_argument("--n_neigh", default=15, type=int,
                        help="The number of neighbors selected when constructing a spatial neighbor graph. default, 15.")
    parser.add_argument("--is_undirected", default=True, type=bool,
                        help="Whether the constructed spatial neighbor graph is undirected graph, default, True.")
    parser.add_argument("--latent_dims", default=100, type=int,
                        help="The number of embedding dimensions, default, 100.")
    parser.add_argument("--is_verbose", default=True, type=bool,
                        help="Whether the detail information is print, default, True.")
    parser.add_argument("--seed", default=42, type=int, help="Random seed")
    parser.add_argument("--gpu", default=0, type=Union[int, str, None],
                        help="Whether the GPU device is using to train spatialign.")
    parser.add_argument("--save_path", default="./output", type=str,
                        help="The path of alignment dataset and saved spatialign.")

    # training parameters
    parser.add_argument("--lr", default=1e-3, type=float, help="Learning rate, default, 1e-3.")
    parser.add_argument("--max_epoch", default=500, type=int, help="The number of maximum epochs, default, 500.")
    parser.add_argument("--alpha", default=0.5, type=float, help="The momentum parameter, default, 0.5")
    parser.add_argument("--patient", default=15, type=int, help="Early stop parameter, default, 15.")
    parser.add_argument("--tau1", default=0.2, type=float,
                        help="Instance level and pseudo prototypical cluster level contrastive learning parameters, default, 0.2")
    parser.add_argument("--tau2", default=1., type=float,
                        help="Pseudo prototypical cluster entropy parameter, default, 1.")
    parser.add_argument("--tau3", default=0.5, type=float,
                        help="Cross-batch instance self-supervised learning parameter, default, 0.5")

    args = parser.parse_args()
    args.data_path = ["/dataset/stereo_olfactory_bulb_ann.h5ad",
                      "/dataset/visium_olfactory_bulb_ann.h5ad"]
    args.is_norm_log = True
    args.is_verbose = False

    args.save_path = "/dataset/output"

    model = Spatialign(*args.data_path,
                       min_genes=args.min_genes,
                       min_cells=args.min_cells,
                       batch_key=args.batch_key,
                       is_norm_log=args.is_norm_log,
                       is_scale=args.is_scale,
                       is_hvg=args.is_hvg,
                       is_reduce=args.is_reduce,
                       n_pcs=args.n_pcs,
                       n_hvg=args.n_hvg,
                       n_neigh=args.n_neigh,
                       is_undirected=args.is_undirected,
                       latent_dims=args.latent_dims,
                       tau1=args.tau1,
                       tau2=args.tau2,
                       tau3=args.tau3,
                       is_verbose=args.is_verbose,
                       seed=args.seed,
                       gpu=args.gpu,
                       save_path=args.save_path)

    model.train(lr=args.lr,
                max_epoch=args.max_epoch,
                alpha=args.alpha,
                patient=args.patient)

    model.alignment()
