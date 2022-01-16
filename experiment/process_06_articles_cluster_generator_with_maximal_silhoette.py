# -*- coding: utf-8 -*-
"""process_06_articles_cluster_generator_with_maximal_silhoette.py

@author    Kataoka Nagi (calm1836[at]gmail.com)
@brief     calc best article cluster with evidence embed & silhouette-coefficient
# nation-id;article-id;sentence-id;e;feature-x;feature-y;sent-1#nation-id;article-id;sentence-id;c;feature-x;feature-y;[feature-array];sent-2...\n
@note      in: nation-id;article-id;[e-embedding]
@note      in : process-05_calced-sentences-features.txt
@note      out : process-06_articles-cluster_embeds-pdist.txt
@note      out : process-06_articles-cluster/process-06_articles-cluster.txt
@note      out : process-06_articles-cluster_dendrogram.png
@note      out : process-06_articles-cluster_color_dendrogram.png
@note      out : process-06_articles-cluster_result.csv
@note      out : process-06_articles-cluster_threshold-dependencies.png
@note      out : process-06_articles-cluster_num_of_cluster.png
@note      out : process-06_articles-cluster_num-of-clusters-dependency-on-silhouette-coefficient.png
@note      python3 process_06_articles_cluster_generator_with_maximal_silhoette.py
@date      2022-01-15 13:59:47
@version   1.0
@history   add
@see       [階層的クラスタリングとシルエット係数](https://qiita.com/maskot1977/items/a35ac2fdc2c7448ee526#%E9%9A%8E%E5%B1%A4%E7%9A%84%E3%82%AF%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%AA%E3%83%B3%E3%82%B0)
@see       [階層的クラスタリングでユークリッド距離とコサイン類似度の結果を比べてみる](https://irukanobox.blogspot.com/2018/08/blog-post.html)
@see       [scipyで距離行列を計算する](https://analytics-note.xyz/programming/scipy-pdist/)
@copyright (c) 2021 Kataoka Nagi

"""

import random
from scipy.cluster import hierarchy
from matplotlib.pyplot import cm
from scipy.spatial.distance import squareform
import math
import matplotlib.pyplot as plt
from utils.log import Log as log
import time
import datetime
from argparse import ArgumentParser
import re
from scipy.cluster.hierarchy import linkage, dendrogram
import numpy as np
import pandas as pd
from scipy.spatial.distance import pdist
import matplotlib as mpl

METRIC = "cosine"
METHOD = "ward"

TITLE_SIZE = 48
LABEL_TITLE_SIZE = 36
LABEL_SIZE = 28

REDUCED_NUM = 10000
RANDOM_SEED = 2021

NUM_OF_CLUSTER = 3650

log.d("METRIC:", METRIC)
log.d("METHOD:", METHOD)
log.v("TITLE_SIZE:", TITLE_SIZE)
log.v("LABEL_TITLE_SIZE:", LABEL_TITLE_SIZE)
log.v("LABEL_SIZE:", LABEL_SIZE)
log.d("REDUCED_NUM:", REDUCED_NUM)
log.d("RANDOM_SEED:", RANDOM_SEED)
log.v("NUM_OF_CLUSTER:", NUM_OF_CLUSTER)


def main():
    articles_dir = "./covid-19-news-articles/process-05_calced-sentences-features.txt"
    embeds_pdist_dir = "./covid-19-news-articles/process-06_articles-cluster_embeds-pdist.txt"
    dest_dir = "./covid-19-news-articles/process-06_articles-cluster/process-06_articles-cluster.txt"
    dendrogram_dir = "./covid-19-news-articles/process-06_articles-cluster_dendrogram.png"
    color_dendrogram_dir = "./covid-19-news-articles/process-06_articles-cluster_color_dendrogram.png"
    result_dir = "./covid-19-news-articles/process-06_articles-cluster_result.csv"
    threshold_dependencies_dir = "./covid-19-news-articles/process-06_articles-cluster_threshold-dependencies.png"
    num_of_cluster_dir = "./covid-19-news-articles/process-06_articles-cluster_num_of_cluster.png"
    silhouette_coefficient_dir = "./covid-19-news-articles/process-06_articles-cluster_num-of-clusters-dependency-on-silhouette-coefficient.png"
    exe_time_dir = "./covid-19-news-articles/archive/exe-time/exe-time_process_06_articles_cluster_generator_with_maximal_silhoette.txt"

    log.v(articles_dir)
    log.v(embeds_pdist_dir)
    log.v(dest_dir)
    log.v(dendrogram_dir)
    log.v(color_dendrogram_dir)
    log.v(result_dir)
    log.v(threshold_dependencies_dir)
    log.v(num_of_cluster_dir)
    log.v(silhouette_coefficient_dir)
    log.v(exe_time_dir)

    # debug option
    arg_parser = ArgumentParser(description='execute S-BERT')
    arg_parser.add_argument(
        "-d",
        "--debug",
        help="optional debug",
        action="store_true")
    arg_parser.add_argument(
        "-r",
        "--reduce",
        help="reduce data",
        action="store_true")
    arg = arg_parser.parse_args()
    do_debug = arg.debug
    reduce_data = arg.reduce

    log.v(do_debug)
    log.v(reduce_data)

    if reduce_data:
        log.d("*** edit DEST_DIRS according to --reduce ***")
        replace_str = "_reduced-data-to-" + str(REDUCED_NUM)
        embeds_pdist_dir = re.sub(
            "\\.txt",
            replace_str + ".txt",
            embeds_pdist_dir)
        dest_dir = re.sub("\\.txt", replace_str + ".txt", dest_dir)
        dendrogram_dir = re.sub("\\.png", replace_str + ".png", dendrogram_dir)
        color_dendrogram_dir = re.sub(
            "\\.png", replace_str + ".png", color_dendrogram_dir)
        result_dir = re.sub("\\.csv", replace_str + ".csv", result_dir)
        threshold_dependencies_dir = re.sub(
            "\\.png", replace_str + ".png", threshold_dependencies_dir)
        num_of_cluster_dir = re.sub(
            "\\.png", replace_str + ".png", num_of_cluster_dir)
        silhouette_coefficient_dir = re.sub(
            "\\.png", replace_str + ".png", silhouette_coefficient_dir)
        exe_time_dir = re.sub("\\.txt", replace_str + ".txt", exe_time_dir)

    if do_debug:
        log.d("*** edit DEST_DIRS according to --debug ***")
        articles_dir = re.sub("\\.txt", "_debug.txt", articles_dir)
        embeds_pdist_dir = re.sub("\\.txt", "_debug.txt", embeds_pdist_dir)
        dest_dir = re.sub("\\.txt", "_debug.txt", dest_dir)
        dendrogram_dir = re.sub("\\.png", "_debug.png", dendrogram_dir)
        color_dendrogram_dir = re.sub(
            "\\.png", "_debug.png", color_dendrogram_dir)
        result_dir = re.sub("\\.csv", "_debug.csv", result_dir)
        threshold_dependencies_dir = re.sub(
            "\\.png", "_debug.png", threshold_dependencies_dir)
        num_of_cluster_dir = re.sub("\\.png", "_debug.png", num_of_cluster_dir)
        silhouette_coefficient_dir = re.sub(
            "\\.png", "_debug.png", silhouette_coefficient_dir)
        exe_time_dir = re.sub("\\.txt", "_debug.txt", exe_time_dir)

    ##################################################
    log.d("*** import articles ***")
    ##################################################

    # nation-n;article-n;[e-embedding]
    # nation-n;article-n;sentence-id;e;feature-x;feature-y;sent-1#...\n
    article_info_or_sentences = []

    with open(articles_dir, "r", encoding="utf_8") as f:
        article_info_or_sentences = f.readlines()
        log.v("articles:")
        log.v("article_info_or_sentences[0]:", article_info_or_sentences[0])
        log.v("article_info_or_sentences[1]:", article_info_or_sentences[1])
        log.v("article_info_or_sentences[2]:", article_info_or_sentences[2])
        log.v()

    ##################################################
    log.d("*** extract nation id, article id, & article embedding ***")
    log.d("*** & save lines by each articles ***")
    ##################################################
    articles_lines = []  # [[lines eacch articles], ...]
    nation_and_article_ids = []  # ["IN;n"]
    article_embeds = []  # [[2.50864863e-01, 9.60696563e-02, ...], ...]
    NATION_ID_IDX = 0
    ARTICLE_ID_IDX = 1
    EMBED_IDX = 2

    # nation-n;article-n;[e-embedding]
    # nation-n;article-n;sentence-id;e;feature-x;feature-y;sent-1#...\n
    for article_info_or_sentence in article_info_or_sentences:

        splits_with_semicolon = article_info_or_sentence.split(';')
        len_splits_with_semicolon = len(splits_with_semicolon)

        # article info
        if len_splits_with_semicolon == 3:
            # extract nation_and_article_ids
            nation_id = splits_with_semicolon[NATION_ID_IDX]
            article_id = splits_with_semicolon[ARTICLE_ID_IDX]
            ids = nation_id + ';' + article_id
            nation_and_article_ids.append(ids)

            # extract article_embeds
            article_embed_str = splits_with_semicolon[EMBED_IDX]
            article_embed_str = article_embed_str.lstrip('[ ')
            article_embed_str = article_embed_str.rstrip(' ]\n')
            article_embed_strs = article_embed_str.split()
            article_embed = [float(embed_str)
                             for embed_str in article_embed_strs]
            article_embeds.append(article_embed)

            # extract lines by each articles
            articles_lines.append(article_info_or_sentence)

        # sentence info
        elif len_splits_with_semicolon == 7 or len_splits_with_semicolon == 8:
            # extract lines by each articles
            articles_lines[-1] += article_info_or_sentence
        # error
        else:
            log.e(
                "unsuspected len_splits_with_semicolon: ",
                len_splits_with_semicolon)
            exit()

    log.v("nation_and_article_ids[0]: ", nation_and_article_ids[0])
    log.v("article_embeds[0]: ", article_embeds[0])
    log.v("articles_lines[0]: ", articles_lines[0])
    log.v("articles_lines[-1]: ", articles_lines[-1])
    log.v()

    # reduce data num (because of memory size error)
    if reduce_data:
        shuffle_idxs = list(range(len(nation_and_article_ids)))
        random.seed(RANDOM_SEED)
        random.shuffle(shuffle_idxs)
        nation_and_article_ids = [
            nation_and_article_ids[i] for i in shuffle_idxs[:REDUCED_NUM]]
        article_embeds = [article_embeds[i]
                          for i in shuffle_idxs[:REDUCED_NUM]]
        articles_lines = [articles_lines[i]
                          for i in shuffle_idxs[:REDUCED_NUM]]
        log.v("nation_and_article_ids[:10]: ",
              nation_and_article_ids[:(10 % REDUCED_NUM)])
        log.v("article_embeds[0]: ", article_embeds[0])
        log.v("articles_lines[0]: ", articles_lines[0])
        log.v()

    ##################################################
    log.d("*** clustering (substitute article_embeds) ***")
    ##################################################

    # time mesurement: start
    clustering_start_time = time.time()

    # exe
    # result1 = linkage(article_embeds, metric=METRIC, method=METHOD)
    embeds_pdist = pdist(article_embeds, metric=METRIC)
    result1 = linkage(embeds_pdist, method=METHOD)

    # print time
    clustering_time = time.time() - clustering_start_time
    log.d("clustering time (sec):", clustering_time)

    # save embed pdist
    with open(embeds_pdist_dir, "w+", encoding="utf_8") as f:
        embeds_pdist_2_str = [str(e) for e in embeds_pdist]
        f.write("\n".join(embeds_pdist_2_str))

    # debug
    embeds_square_form = squareform(embeds_pdist)
    log.v("embeds_pdist[0]:", embeds_pdist[0])
    log.v("embeds_square_form[0]:", embeds_square_form[0])
    log.v("embeds_square_form[1]:", embeds_square_form[1])
    log.v("embeds_square_form[2]:", embeds_square_form[2])

    ##################################################
    log.d("*** print clustering result ***")
    ##################################################
    result_df = pd.DataFrame(result1)
    result_df.to_csv(result_dir)

    if do_debug:
        log.v("result_df:", result_df)
    log.v("result_df[0][0] (1st node      ) :", result_df[0][0])
    log.v("result_df[1][0] (2nd node      ) :", result_df[1][0])
    log.v("result_df[2][0] (nodes distance) :", result_df[2][0])
    log.v("result_df[3][0] (cluster_id    ) :", result_df[3][0])

    ##################################################
    log.d("*** draw num of clusters dependency on silhouette coefficient ***")
    log.d("*** & calc best them ***")
    ##################################################
    # time mesurement: start
    drawing_num_and_silhouette_start_time = time.time()

    distance_matrix = get_distance_matrix(result_df)
    best_num_of_cluster = 0
    best_cluster_by_number = []
    max_silhouette_coefficient = -100100100
    x = []
    y = []
    for num_of_cluster in range(2, len(result_df)):
        cluster_by_number = get_cluster_by_number(result1, num_of_cluster)
        silhouette_coefficient = silhouette_coefficient2(
            cluster_by_number, distance_matrix)
        if silhouette_coefficient > max_silhouette_coefficient:
            best_num_of_cluster = num_of_cluster
            best_cluster_by_number = cluster_by_number
            max_silhouette_coefficient = silhouette_coefficient
        x.append(num_of_cluster)
        y.append(silhouette_coefficient)

    silhouette_fig = plt.figure(figsize=(19.2, 14.4))
    plt.plot(x, y)
    plt.xlabel("Num of Clusters", fontsize=LABEL_TITLE_SIZE)
    plt.ylabel("Silhouette Coefficient", fontsize=LABEL_TITLE_SIZE)
    plt.grid()
    plt.tick_params(labelsize=LABEL_SIZE)
    # plt.show()
    silhouette_fig.savefig(silhouette_coefficient_dir)

    # print time
    drawing_num_and_silhouette_time = time.time(
    ) - drawing_num_and_silhouette_start_time
    log.d("drawing num and silhouette time (sec):",
          drawing_num_and_silhouette_time)

    log.d("best_num_of_cluster: ", best_num_of_cluster)
    log.d("max_silhouette_coefficient: ", max_silhouette_coefficient)
    log.v("best_cluster_by_number: ", best_cluster_by_number)
    log.v()

    ##################################################
    log.d("*** draw threshold dependency ***")
    ##################################################
    # time mesurement: start
    drawing_threshold_dependency_start_time = time.time()

    # exe
    best_threshold = draw_threshold_dependency(
        result1,
        threshold_dependencies_dir,
        best_num_of_cluster)
    log.d("best_threshold:", best_threshold)

    # print time
    drawing_threshold_dependency_time = time.time(
    ) - drawing_threshold_dependency_start_time
    log.d("drawing threshold dependency time (sec):",
          drawing_threshold_dependency_time)

    ##################################################
    log.d("*** draw dendrogram ***")
    ##################################################

    # time mesurement: start
    drawing_dendrogram_start_time = time.time()

    # exe
    dendrogram_fig = plt.figure(figsize=(14.4, 19.2))
    dendrogram(
        result1,
        orientation='right',
        labels=[''] * len(nation_and_article_ids),
        # labels=nation_and_article_ids,
        color_threshold=0.0
    )
    # plt.title(
    #     "Article Dendrogram by Evidence Sentences",
    #     fontsize=TITLE_SIZE - 6)
    plt.xlabel("Threshold", fontsize=LABEL_TITLE_SIZE)
    plt.ylabel("Article ID", fontsize=LABEL_TITLE_SIZE)
    plt.grid()
    plt.tick_params(labelsize=LABEL_SIZE)
    # plt.show()
    dendrogram_fig.savefig(dendrogram_dir)

    # exe color ver

    # set color
    # @see https://www.webdevqa.jp.net/ja/python/python%EF%BC%88linkcolorfunc%EF%BC%9F%EF%BC%89%E3%81%AEscipy%E6%A8%B9%E7%8A%B6%E5%9B%B3%E3%81%AE%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%A0%E3%82%AF%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC%E3%82%AB%E3%83%A9%E3%83%BC/825416841/
    # cmap = cm.Rainbow(np.linspace(0, 1, best_num_of_cluster))
    # link_cols = [mpl.colors.rgb2hex(rgb[:3]) for rgb in cmap]

    color_dendrogram_fig = plt.figure(figsize=(14.4, 19.2))
    dendrogram(
        result1,
        orientation='right',
        labels=[''] * len(nation_and_article_ids),
        # labels=nation_and_article_ids,
        color_threshold=best_threshold,
        # link_color_func=lambda x: link_cols[x]
    )
    # plt.title(
    #     "Article Dendrogram by Evidence Sentences",
    #     fontsize=TITLE_SIZE - 6)
    plt.xlabel("Threshold", fontsize=LABEL_TITLE_SIZE)
    plt.ylabel("Article ID", fontsize=LABEL_TITLE_SIZE)
    plt.grid()
    plt.tick_params(labelsize=LABEL_SIZE)
    # plt.show()
    color_dendrogram_fig.savefig(color_dendrogram_dir)

    # print time
    drawing_dendrogram_time = time.time() - drawing_dendrogram_start_time
    log.d("drawing dendrogram time (sec):", drawing_dendrogram_time)

    ##################################################
    log.d("*** draw best_num_of_cluster ***")
    ##################################################
    num_of_cluster_fig = plt.figure(figsize=(19.2, 14.4))
    plt.hist(best_cluster_by_number)
    plt.xlabel("Cluster ID", fontsize=LABEL_TITLE_SIZE)
    plt.ylabel("Num of Article", fontsize=LABEL_TITLE_SIZE)
    plt.tick_params(labelsize=LABEL_SIZE)
    plt.grid()
    num_of_cluster_fig.savefig(num_of_cluster_dir)

    ##################################################
    log.d("*** save lines in each cluster with best_cluster_by_number ***")
    ##################################################
    clusters_articles = [''] * best_num_of_cluster
    for article_id, cluster_id in enumerate(best_cluster_by_number):
        clusters_articles[cluster_id] += articles_lines[article_id]

    # write
    for _, cluster_id in enumerate(best_cluster_by_number):
        dest_dir_each_cluster_id = re.sub(
            "\\.txt", "_" + str(cluster_id) + ".txt", dest_dir)
        with open(dest_dir_each_cluster_id, "w+", encoding="utf_8") as f:
            f.write(clusters_articles[cluster_id])

    ##################################################
    log.d("*** save time logs ***")
    ##################################################

    # write time
    with open(exe_time_dir, "a+", encoding="utf_8") as f:
        f.write(str(datetime.datetime))
        f.write("clustering_time (sec): ")
        f.write(str(clustering_time) + "\n")

        f.write("drawing_dendrogram_time (sec): ")
        f.write(str(drawing_dendrogram_time) + "\n")

        f.write("drawing_threshold_dependency_time (sec): ")
        f.write(str(drawing_threshold_dependency_time) + "\n")

        f.write("drawing_num_and_silhouette_time (sec): ")
        f.write(str(drawing_num_and_silhouette_time) + "\n")

        f.write("\n")

    ##################################################
    ##################################################


def draw_threshold_dependency(
        result,
        threshold_dependencies_dir,
        best_num_of_cluster):
    n_clusters = len(result)
    n_samples = len(result)
    df1 = pd.DataFrame(result)
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    best_threshold = 0.0
    for i in range(len(result) - 1):
        n1 = int(result[i][0])
        n2 = int(result[i][1])
        val = result[i][2]
        n_clusters -= 1
        x1.append(val)
        x2.append(val)
        y1.append(n_clusters)
        y2.append(float(n_samples) / float(n_clusters))
        if n_clusters == best_num_of_cluster:
            best_threshold = val

    dependencies_fig = plt.figure(figsize=(19.2, 14.4))
    plt.subplot(2, 1, 1)
    plt.plot(x1, y1, 'yo-')
    # plt.title(
    #     'Threshold Dependency of Hierarchical Clustering',
    #     fontsize=TITLE_SIZE)
    plt.ylabel('Num of Clusters', fontsize=LABEL_TITLE_SIZE)
    plt.grid()
    plt.tick_params(labelsize=LABEL_SIZE)
    plt.subplot(2, 1, 2)
    plt.plot(x2, y2, 'ro-')
    plt.xlabel('Threshold', fontsize=LABEL_TITLE_SIZE)
    plt.ylabel('Average of Cluster Size', fontsize=LABEL_TITLE_SIZE)
    plt.grid()
    plt.tick_params(labelsize=LABEL_SIZE)
    # plt.show()
    dependencies_fig.savefig(threshold_dependencies_dir)
    return best_threshold


# 指定したクラスタ数でクラスタを得る関数を作る。
def get_cluster_by_number(result, number):
    output_clusters = []
    x_result, y_result = result.shape
    n_clusters = x_result + 1
    cluster_id = x_result + 1
    father_of = {}
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    for i in range(len(result) - 1):
        n1 = int(result[i][0])
        n2 = int(result[i][1])
        val = result[i][2]
        n_clusters -= 1
        if n_clusters >= number:
            father_of[n1] = cluster_id
            father_of[n2] = cluster_id

        cluster_id += 1

    cluster_dict = {}
    for n in range(x_result + 1):
        if n not in father_of:
            output_clusters.append([n])
            continue

        n2 = n
        m = False
        while n2 in father_of:
            m = father_of[n2]
            #print [n2, m]
            n2 = m

        if m not in cluster_dict:
            cluster_dict.update({m: []})
        cluster_dict[m].append(n)

    output_clusters += cluster_dict.values()

    output_cluster_id = 0
    output_cluster_ids = [0] * (x_result + 1)
    for cluster in sorted(output_clusters):
        for i in cluster:
            output_cluster_ids[i] = output_cluster_id
        output_cluster_id += 1

    return output_cluster_ids


def get_distance_matrix(df):
    distance_matrix = []
    for i in range(len(df)):
        vec1 = df.iloc[i, :].values
        distance_array = []
        for j in range(len(df)):
            vec2 = df.iloc[j, :].values
            dist = 0.
            for v1, v2 in zip(vec1, vec2):
                dist += (v1 - v2) ** 2
            distance_array.append(math.sqrt(dist))
        distance_matrix.append(distance_array)
    return distance_matrix


def silhouette_coefficient2(clusters, distance_matrix):
    do_debug = False
    if do_debug:
        log.v("clusters:", clusters)
        log.v("distance_matrix:", distance_matrix)
        log.v("len(clusters):", len(clusters))
        log.v("len(distance_matrix):", len(distance_matrix))
        log.v("clusters[0]:", clusters[0])
        log.v("distance_matrix[0]:", distance_matrix[0])
    a_same = []
    b_diff = []
    for i, j in enumerate(clusters):
        for k, l in enumerate(clusters):
            if i < k:
                # log.v("i, k:", i, k)
                if k == len(distance_matrix):
                    continue  # kataoka edit
                dist = distance_matrix[i][k]
                if j == l:  # same cluster
                    a_same.append(dist)
                else:  # different cluster
                    b_diff.append(dist)
    a = sum(a_same) / len(a_same)
    b = sum(b_diff) / len(b_diff)
    return (b - a) / max(b, a)


if __name__ == "__main__":
    main()
