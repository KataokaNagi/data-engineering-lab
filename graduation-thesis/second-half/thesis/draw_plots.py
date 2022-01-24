# -*- coding: utf-8 -*-
# @see https://www.albert2005.co.jp/knowledge/data_mining/cluster/hierarchical_clustering
# @see https://pythondatascience.plavox.info/matplotlib/%E8%89%B2%E3%81%AE%E5%90%8D%E5%89%8D#google_vignette

from os import X_OK
import numpy as np
import matplotlib.pyplot as plt

# save dir
SAVE_FIG_DIR = "./img/plots_example.png"

# title
LABEL_TITLE_X = "Feature $x_1$"
LABEL_TITLE_Y = "Feature $x_2$"

# size
FIG_SIZE_X = 19.2 * 2 / 3
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
MARKER_LABELS = [
    'A',
    'B',
    'C',
    'D',
    'E',
]
MARKER_SIZE = 20
MARKER_COLOR = "black"
ANNOTATE_COLOR = "black"
# ANNOTATE_COLOR = "dimgray"
ANNOTATE_SIZE = LABEL_SIZE_X
ANNOTATE_LOC_X = 0.2
ANNOTATE_LOC_Y = 0.2

# グラフの設定
fig = plt.figure(figsize=(FIG_SIZE_X, FIG_SIZE_Y))
plt.tick_params(axis='x', labelsize=LABEL_SIZE_X)
plt.tick_params(axis='y', labelsize=LABEL_SIZE_Y)
plt.xlabel(LABEL_TITLE_X, fontsize=LABEL_TITLE_SIZE_X)
plt.ylabel(LABEL_TITLE_Y, fontsize=LABEL_TITLE_SIZE_Y)

X_IDX = 0
Y_IDX = 1
for i, plot in enumerate(PLOTS):
    x = plot[X_IDX]
    y = plot[Y_IDX]
    plt.plot(
        x,
        y,
        marker='.',
        markersize=MARKER_SIZE,
        color=MARKER_COLOR)  # プロット
    plt.annotate(
        MARKER_LABELS[i], xy=(
            x, y), size=ANNOTATE_SIZE, xytext=(
            x + ANNOTATE_LOC_X, y + ANNOTATE_LOC_Y),
        color=ANNOTATE_COLOR)

plt.xlim(RANGE_X_LEFT, RANGE_X_RIGHT)  # x軸の範囲
plt.ylim(RANGE_Y_LEFT, RANGE_Y_RIGHT)  # y軸の範囲
plt.grid()  # グリッド描画
# plt.show()  # グラフを出力

fig.savefig(SAVE_FIG_DIR)
