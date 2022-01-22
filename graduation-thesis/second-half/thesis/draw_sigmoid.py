# -*- coding: utf-8 -*-
# @see https://algorithm.joho.info/programming/python/numpy-sigmoid/
# @see https://tech-market.org/matplotlib-latex/
# @see https://python-remrin.hatenadiary.jp/entry/2017/05/27/114816
import numpy as np
import matplotlib.pyplot as plt

# save dir
SAVE_FIG_DIR = "./img/sigmoid.png"

# title
LABEL_TITLE_X = "$t$"
LABEL_TITLE_Y = "$\\sigma(t)=\\frac{1}{1+\\exp(-t)}$"
LABEL_TITLE_Y_LOC = "upper left"

# size
FIG_SIZE_X = 19.2
FIG_SIZE_Y = 10

LABEL_SIZE_X = 32
LABEL_SIZE_Y = 32

LABEL_TITLE_SIZE_X = 40
LABEL_TITLE_SIZE_Y = 40

# draw range
RANGE_X_LEFT = -10
RANGE_X_RIGHT = 10
RANGE_Y_LEFT = -0.1
RANGE_Y_RIGHT = 1.1

# plot info
PLOT_STEPS = 0.1


# xの値（-10～10で0.1刻みで配列生成）
x = np.arange(RANGE_X_LEFT, RANGE_X_RIGHT, PLOT_STEPS)

#　シグモイド関数
y = 1 / (1 + np.exp(-x))

# グラフの設定
fig = plt.figure(figsize=(FIG_SIZE_X, FIG_SIZE_Y))
plt.tick_params(axis='x', labelsize=LABEL_SIZE_X)
plt.tick_params(axis='y', labelsize=LABEL_SIZE_Y)
plt.xlabel(LABEL_TITLE_X, fontsize=LABEL_TITLE_SIZE_X)
# plt.ylabel(LABEL_TITLE_Y, fontsize=LABEL_TITLE_SIZE_Y)

plt.plot(x, y, label=LABEL_TITLE_Y)  # プロット
plt.xlim(RANGE_X_LEFT, RANGE_X_RIGHT)  # x軸の範囲
plt.ylim(RANGE_Y_LEFT, RANGE_Y_RIGHT)  # y軸の範囲
plt.grid()  # グリッド描画
# plt.show()  # グラフを出力

plt.legend(
    fontsize=LABEL_TITLE_SIZE_Y,
    loc=LABEL_TITLE_Y_LOC)
fig.savefig(SAVE_FIG_DIR)
