# -*- coding: utf-8 -*-
"""
Authors: Brandstetter, Schäfl, Schörgenhumer
Date: 02-10-2023

This file is part of the "Hands on AI I" lecture material. The following
copyright statement applies to all code within this file.

Copyright statement: 
This material, no matter whether in printed or electronic form, may be used for
personal and non-commercial educational use only. Any reproduction of this
material, no matter whether as a whole or in parts, no matter whether in printed
or in electronic form, requires explicit prior acceptance of the authors.
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import sklearn
import sys
import warnings

from distutils.version import LooseVersion
from IPython.core.display import HTML
from sklearn import datasets
from sklearn.cluster import KMeans, AffinityPropagation
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import scale
from typing import Optional, Sequence

warnings.filterwarnings(
    "ignore",
    category=FutureWarning,
    message=r"is_categorical_dtype is deprecated and will be removed in a future version\. Use isinstance\(dtype, "
            r"CategoricalDtype\) instead",
    module="seaborn"
)
warnings.filterwarnings(
    "ignore",
    category=FutureWarning,
    message=r"use_inf_as_na option is deprecated and will be removed in a future version\. Convert inf values to NaN "
            r"before operating instead\.",
    module="seaborn"
)


def setup_jupyter() -> HTML:
    """
    Setup Jupyter notebook. Warning: this may affect all Jupyter notebooks running on the same Jupyter server.

    :return: HTML instance comprising the modified Jupyter attributes
    """
    return HTML(r"""
    <style>
        .output_png {
            display: table-cell;
            text-align: center;
            vertical-align: middle;
        }
        .jp-RenderedImage {
            display: table-cell;
            text-align: center;
            vertical-align: middle;
        }
    </style>
    <p>Setting up notebook ... finished.</p>
    """)


def check_module_versions() -> None:
    """
    Check Python version as well as versions of recommended (partly required) modules.
    """
    python_check = '(\u2713)' if sys.version_info >= (3, 8) else '(\u2717)'
    numpy_check = '(\u2713)' if LooseVersion(np.__version__) >= LooseVersion('1.18') else '(\u2717)'
    pandas_check = '(\u2713)' if LooseVersion(pd.__version__) >= LooseVersion('1.0') else '(\u2717)'
    sklearn_check = '(\u2713)' if LooseVersion(sklearn.__version__) >= LooseVersion('1.2') else '(\u2717)'
    matplotlib_check = '(\u2713)' if LooseVersion(matplotlib.__version__) >= LooseVersion('3.2.0') else '(\u2717)'
    seaborn_check = '(\u2713)' if LooseVersion(sns.__version__) >= LooseVersion('0.10.0') else '(\u2717)'
    print(f'Installed Python version: {sys.version_info.major}.{sys.version_info.minor} {python_check}')
    print(f'Installed numpy version: {np.__version__} {numpy_check}')
    print(f'Installed pandas version: {pd.__version__} {pandas_check}')
    print(f'Installed scikit-learn version: {sklearn.__version__} {sklearn_check}')
    print(f'Installed matplotlib version: {matplotlib.__version__} {matplotlib_check}')
    print(f'Installed seaborn version: {sns.__version__} {seaborn_check}')


def load_wine() -> pd.DataFrame:
    """
    Load wine dataset [1].

    [1] Forina, M. et al, PARVUS - An Extendible Package for Data Exploration, Classification and Correlation.
        Institute of Pharmaceutical and Food Analysis and Technologies, Via Brigata Salerno, 16147 Genoa, Italy.

    :return: wine dataset
    """
    wine_data = datasets.load_wine()
    data = pd.DataFrame(wine_data['data'], columns=wine_data['feature_names'])
    data['cultivator'] = wine_data['target']
    return data


def load_breast_cancer() -> pd.DataFrame:
    """
    Load breast cancer wisconsin (diagnostic) dataset [1].
    
    Classes: 0 = malignant, 1 = benign
    
    [1] W.N. Street, W.H. Wolberg and O.L. Mangasarian. Nuclear feature extraction for breast tumor diagnosis.
        IS&T/SPIE 1993 International Symposium on Electronic Imaging: Science and Technology, volume 1905,
        pages 861-870, San Jose, CA, 1993.
    """
    data, targets = datasets.load_breast_cancer(return_X_y=True, as_frame=True)
    data["diagnosis"] = targets
    return data


def plot_features(data: pd.DataFrame, features: Sequence[str], target_column: Optional[str] = None,
                  sns_kwargs: dict = None) -> None:
    """
    Visualizes the specified features of the dataset via pairwise relationship plots. Optionally,
    the displayed data points can be colored according to the specified ``target_column``.
    
    :param data: dataset containing the features
    :param features: the list of features to visualize
    :param target_column: if specified, color the visualized data points according to this target
    :param sns_kwargs: additional keyword arguments that are passed to ``sns.pairplot`` (must not
        contain any of "data", "vars", "hue")
    """
    assert isinstance(data, pd.DataFrame)
    assert isinstance(features, Sequence)
    assert sns_kwargs is None or isinstance(sns_kwargs, dict)
    assert target_column is None or isinstance(target_column, str)
    if isinstance(features, str):
        features = [features]
    if sns_kwargs is None:
        sns_kwargs = dict(palette="deep")
    sns.pairplot(data=data, vars=features, hue=target_column, **sns_kwargs)


def apply_pca(n_components: int, data: pd.DataFrame, target_column: Optional[str] = None,
              standardize: bool = False) -> pd.DataFrame:
    """
    Apply principal component analysis (PCA) on specified dataset and down-project data accordingly.

    :param n_components: amount of (top) principal components involved in down-projection
    :param data: dataset to down-project
    :param target_column: if specified, append target column to resulting, down-projected dataset
    :param standardize: If True, standardize the data (zero mean, unit variance) before applying PCA
    :return: down-projected dataset
    """
    assert (type(n_components) == int) and (n_components >= 1)
    assert type(data) == pd.DataFrame
    assert ((type(target_column) == str) and (target_column in data)) or (target_column is None)
    if target_column is not None:
        raw_data = data.drop(columns=target_column)
        if standardize:
            raw_data = scale(raw_data)
        projected_data = pd.DataFrame(PCA(n_components=n_components).fit_transform(raw_data), index=data.index)
        projected_data[target_column] = data[target_column]
    else:
        if standardize:
            data = scale(data)
        projected_data = pd.DataFrame(PCA(n_components=n_components).fit_transform(data), index=data.index)
    return projected_data


def apply_tsne(n_components: int, data: pd.DataFrame, target_column: Optional[str] = None,
               perplexity: float = 10.0, standardize: bool = False) -> pd.DataFrame:
    """
    Apply t-distributed stochastic neighbor embedding (t-SNE) on specified dataset and down-project data accordingly.

    :param n_components: dimensionality of the embedding space
    :param data: dataset to down-project
    :param target_column: if specified, append target column to resulting, down-projected dataset
    :param perplexity: this term is closely related to the number of nearest neighbors to consider
    :param standardize: If True, standardize the data (zero mean, unit variance) before applying t-SNE
    :return: down-projected dataset
    """
    assert (type(n_components) == int) and (n_components >= 1)
    assert type(data) == pd.DataFrame
    assert ((type(target_column) == str) and (target_column in data)) or (target_column is None)
    assert (type(perplexity) == float) or (type(perplexity) == int)
    if target_column is not None:
        raw_data = data.drop(columns=target_column)
        if standardize:
            raw_data = scale(raw_data)
        projected_data = pd.DataFrame(TSNE(n_components=n_components, perplexity=float(perplexity), learning_rate=200,
                                           init="random").fit_transform(raw_data), index=data.index)
        projected_data[target_column] = data[target_column]
    else:
        if standardize:
            data = scale(data)
        projected_data = pd.DataFrame(TSNE(n_components=n_components, perplexity=float(perplexity), learning_rate=200,
                                           init="random").fit_transform(data), index=data.index)
    return projected_data


def apply_k_means(k: int, data: pd.DataFrame, standardize: bool = False) -> pd.DataFrame:
    """
    Apply k-means clustering algorithm on the specified data.

    :param k: amount of clusters
    :param data: data used for clustering
    :param standardize: If True, standardize the data (zero mean, unit variance) before applying k-means
    :return: predicted cluster per dataset entry
    """
    assert (type(k) == int) and (k >= 1)
    assert type(data) == pd.DataFrame
    if standardize:
        data = scale(data)
    return KMeans(n_clusters=k, n_init="auto").fit_predict(data)


def apply_affinity_propagation(data: pd.DataFrame, standardize: bool = False) -> pd.DataFrame:
    """
    Apply affinity propagation clustering algorithm on the specified data.

    :param data: data used for clustering
    :param standardize: If True, standardize the data (zero mean, unit variance) before applying affinity propagation
    :return: predicted cluster per dataset entry
    """
    assert type(data) == pd.DataFrame
    if standardize:
        data = scale(data)
    return AffinityPropagation(affinity='euclidean', random_state=None).fit_predict(data)


def plot_points_2d(data: pd.DataFrame, target_column: Optional[str] = None, legend: bool = True,
                   hide_ticks: bool = True, sns_kwargs: dict = None, **kwargs) -> None:
    """
    Visualize data points in a two-dimensional plot, optionally colored according to ``target_column``.

    :param data: dataset to visualize
    :param target_column: optional target column to be used for color-coding
    :param legend: flag for displaying a legend
    :param sns_kwargs: additional keyword arguments that are passed to ``sns.scatterplot`` (must not
        contain any of "data", "x", "y", "hue", "legend", "ax)
    :param hide_ticks: If True, x-ticks, y-ticks and the grid are hidden
    :param kwargs: keyword arguments that are passed to ``plt.subplots``
    """
    assert (type(data) == pd.DataFrame) and (data.shape[1] in [2, 3])
    assert (target_column is None) or ((data.shape[1] == 3) and (data.columns[2] == target_column))
    assert type(legend) == bool
    assert sns_kwargs is None or isinstance(sns_kwargs, dict)
    if legend:
        legend = "auto"
    if sns_kwargs is None:
        sns_kwargs = dict(palette="deep")
    _, ax = plt.subplots(**kwargs)
    sns.scatterplot(data=data, x=0, y=1, hue=target_column, legend=legend, ax=ax, **sns_kwargs)
    if hide_ticks:
        ax.set_xticks([])
        ax.set_yticks([])
    ax.set_xlabel(None)
    ax.set_ylabel(None)
