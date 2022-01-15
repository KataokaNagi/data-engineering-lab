# import re

# DIST_DIRS = [
#     "./covid-19-news-articles/india-articles_preprocess_03_spilt-sentences.txt",
#     "./covid-19-news-articles/japan-articles_preprocess_03_spilt-sentences.txt",
#     "./covid-19-news-articles/korea-articles_preprocess_03_spilt-sentences.txt"
#     # "./covid-19-news-articles/uk-articles_preprocess_03_spilt-sentences.txt"
# ]

# do_debug = True
# use_spacy = False
# use_stanza = True

# # edit DIST_SIRS according to options
# for i, dir in enumerate(DIST_DIRS):
#     if use_spacy:
#         DIST_DIRS[i] = re.sub("\.txt","_with-spacy.txt", dir)
#     if use_stanza:
#         DIST_DIRS[i] = re.sub("\.txt","_with-stanza.txt", dir)
#         print("use stanza")

#     if do_debug:
#         DIST_DIRS[i] = re.sub("\.txt","_debug.txt", dir)
#     # print(dir)
#     print(DIST_DIRS[i])

# for dir in DIST_DIRS:
#     print(dir)

##################################################

# from argparse import ArgumentParser

# ap1 = ArgumentParser(description='one')
# ap2 = ArgumentParser(description='two')

# ap1.add_argument(
#     "-o",
#     "--one",
#     help="one description",
#     action="store_true")
# # ap2.add_argument(
# #     "-t",
# #     "--two",
# #     help="two description",
# #     action="store_true")

# arg1 = ap1.parse_args()
# # arg2 = ap2.parse_args()

# print("foo")

# if arg1.one:
#     print("one")

# if arg2.two:
#     print("two")

##################################################

# import utils

# utils.log.Log.v("vorbose")
# utils.log.Log.d("debug")
# utils.log.Log.e("error")
# utils.log.Log.w("worning")

# from utils.log import Log as log

# log.v("vorbose")
# log.d("debug")
# log.e("error")
# log.w("worning")

##################################################

# s = "  "
# print("left", s.strip(), "right")

##################################################

# aaa = [[["1", "2"], ["3", "4"]], [["5", "6"], ["7", "8"]]]

# # b = [a for a in aa for aa in aaa]

# # b = [((a) for a in aa) for aa in aaa]

# # b = [aa for aa in aaa]
# # c = [a for a in aa]

# # b = " ".join(aaa)

# b = []
# for _, aa in enumerate(aaa):
#     for _, a in enumerate(aa):
#         b.extend(a)

# print(b)
# # print(c)

##################################################

# @see https://techacademy.jp/magazine/39544
# @see https://techacademy.jp/magazine/22285
import numpy as np
import matplotlib.pyplot as plt

# 1つ目の表示するデータを用意
x1 = [100, 200, 300, 400, 500, 600]
y1 = [10, 20, 30, 50, 80, 130]

# 2つ目の表示するデータを用意(1つ目のデータを利用)
x2 = x1
y2 = x1

fig1 = plt.figure()

# 1つ目のデータをplotメソッドでプロット
plt.plot(x1, y1, color='red', marker='o')


# 2つ目のデータをplotメソッドでプロット
plt.plot(x2, y2, color='blue', marker='v')

plt.show()
fig1.savefig("img1.png")

# matplotlibにあるpyplotというモジュールをインポートして、
# pltという省略した名前で利用できるようにしています。
# numpyというライブラリをインポートして、
# npという省略した名前で利用できるようにしています。

# 平均50、分散20の乱数を10万個作成しています。
# npのrandom
x = np.random.normal(50, 20, 100000)

# 画像のプロット先の準備をします。
# ここでは、Figure(432x288)のようなデータが準備されています。
fig2 = plt.figure()

# plt（matplotlibにあるpyplotというモジュール）の
# histメソッドを利用してヒストグラムの描画をしています。
# xでは、npで生成した乱数を指定しています。
# binsでは、表示する棒の数を指定しています。
# ecでは、barの境目の線の色を指定しています。
plt.hist(x, bins=100, ec='black')

# plot.titleでは、グラフのタイトルを指定しています。
plt.title("normal histogram")
# plot.xlabelでは、x方向のラベルを指定しています。
# x方向とはグラフの横向きの方向です。
plt.xlabel("x")
# plot.ylabelでは、y方向のラベルを指定しています。
# y方向とはグラフの縦向きの方向です。
plt.ylabel("y")
# plt.xlimでは、グラフの表示範囲を指定しています。
# ()で指定しているのは、(Xの最小値, Xの最大値)です。
plt.xlim(-50, 150)
# plt.grid()では、グリッドを表示しています。
plt.grid()
plt.show()

# fig.savefig("img.png")では、
# グラフをimg.pngという名前のファイルに保存しています。
fig2.savefig("img2.png")
