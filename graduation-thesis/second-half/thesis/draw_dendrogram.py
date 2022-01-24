# -*- coding: utf-8 -*-
# @see https://www.albert2005.co.jp/knowledge/data_mining/cluster/hierarchical_clustering
# @see https://pythondatascience.plavox.info/matplotlib/%E8%89%B2%E3%81%AE%E5%90%8D%E5%89%8D#google_vignette
# @see https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.dendrogram.html
# @see https://qiita.com/kusano_t/items/cbdefba373b9a56c66b5

from os import X_OK
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial import distance

# save dir
SAVE_FIG_DIR = "./img/dendrogram_example.png"

# title
LABEL_TITLE_X = "Distance between Clusters"
# LABEL_TITLE_Y = "Feature Label"
LABEL_TITLE_Y = "Data Label"
# LABEL_TITLE_Y = ""

# size
# FIG_SIZE_X = 19.2 * 2 / 3
FIG_SIZE_X = 19.2
FIG_SIZE_Y = 14.4 * 2 / 3

LABEL_SIZE_X = 32
LABEL_SIZE_Y = 32

LABEL_TITLE_SIZE_X = 40
LABEL_TITLE_SIZE_Y = 40

# draw range
RANGE_X_LEFT = 0.1
RANGE_X_RIGHT = 12
RANGE_Y_LEFT = 0.1
RANGE_Y_RIGHT = 12

# plot info
PLOTS = [
    [2, 4],
    [3, 2],
    [6, 3],
    [7, 6],
    [10, 10],
]
# MARKER_LABELS = [
#     'A',
#     'B',
#     'C',
#     'D',
#     'E',
# ]
MARKER_LABELS = [
    '    A    ',
    '    B    ',
    '    C    ',
    '    D    ',
    '    E    ',
]
MARKER_SIZE = 20
# MARKER_COLOR = "dimgray"
MARKER_COLOR = "black"
ANNOTATE_SIZE = LABEL_SIZE_X
ANNOTATE_LOC_X = 0.2
ANNOTATE_LOC_Y = 0.2

# dendrogram info
DISTANCE_METRIC = "euclidean"
CLUSTER_DISTANCE_METHOD = "ward"

# グラフの設定
fig = plt.figure(figsize=(FIG_SIZE_X, FIG_SIZE_Y))

dist_mat = distance.cdist(PLOTS, PLOTS, metric=DISTANCE_METRIC)
clustering_result = linkage(dist_mat, method=CLUSTER_DISTANCE_METHOD)

dendrogram(
    clustering_result,
    orientation='right',
    labels=MARKER_LABELS,
    color_threshold=0.0,
    above_threshold_color=MARKER_COLOR
)
plt.tick_params(axis='x', labelsize=LABEL_SIZE_X)
plt.tick_params(axis='y', labelsize=LABEL_SIZE_Y)
plt.xlabel(LABEL_TITLE_X, fontsize=LABEL_TITLE_SIZE_X)
plt.ylabel(LABEL_TITLE_Y, fontsize=LABEL_TITLE_SIZE_Y)

plt.grid()  # グリッド描画
# plt.show()  # グラフを出力

fig.savefig(SAVE_FIG_DIR)
