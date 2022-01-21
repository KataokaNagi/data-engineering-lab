# -*- coding: utf-8 -*-
"""process_07_sentences_cluster_generator.py

@author    Kataoka Nagi (calm1836[at]gmail.com)
@brief     calc best sentence cluster with claim embeds & silhouette-coefficient
@note      in : process-06_articles-cluster/process-06_articles-cluster.txt
@note      in:  nation-id;article-id;sentence-id;e;feature-x;feature-y;sent-1#nation-id;article-id;sentence-id;c;feature-x;feature-y;[feature-array];sent-2...\n
@note      out : process-07_sentences-cluster_embeds-pdist.txt
@note      out : process-07_sentences-cluster.txt
@note      out : process-07_sentences-cluster_dendrogram.png
@note      out : process-07_sentences-cluster_color_dendrogram.png
@note      out : process-07_sentences-cluster_result.csv
@note      out : process-07_sentences-cluster_threshold-dependencies.png
@note      out : process-07_sentences-cluster_num_of_cluster.png
@note      out : process-07_sentences-cluster_num-of-clusters-dependency-on-silhouette-coefficient.png
@note      python3 process_07_sentences_cluster_generator.py
@date      2022-01-16 11:57:32
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
# LABEL_SIZE = 14

REDUCED_NUM = 959
# REDUCED_NUM = 5000
# REDUCED_NUM = 10000

RANDOM_SEED = 2021

MAX_NUM_OF_CLUSTER_RATE = 0.95

# DRAW_IDS = False
DRAW_IDS = True

# ** REDUCED_NUM = 959 **
# ARTICLES_CLUSTER_ID = 741
# ARTICLES_CLUSTER_ID = 718
# ARTICLES_CLUSTER_ID = 100
# ARTICLES_CLUSTER_ID = 319
ARTICLES_CLUSTER_ID = 19

# ** REDUCED_NUM = 5000 **

# ** REDUCED_NUM = 10000 **


ARTICLES_DIR = "./covid-19-news-articles/process-06_articles-cluster/" +\
    "process-06_articles-cluster_" + \
    "with-maximal-silhoette_" + \
    "reduced-data-to-" + str(REDUCED_NUM) + '/' + \
    "process-06_articles-cluster_" + \
    "with-maximal-silhoette_" + \
    "reduced-data-to-" + str(REDUCED_NUM) + "_" + \
    str(ARTICLES_CLUSTER_ID) + ".txt"

log.d("METRIC:", METRIC)
log.d("METHOD:", METHOD)
log.v("TITLE_SIZE:", TITLE_SIZE)
log.v("LABEL_TITLE_SIZE:", LABEL_TITLE_SIZE)
log.v("LABEL_SIZE:", LABEL_SIZE)
log.d("REDUCED_NUM:", REDUCED_NUM)
log.d("RANDOM_SEED:", RANDOM_SEED)
log.v("MAX_NUM_OF_CLUSTER_RATE:", MAX_NUM_OF_CLUSTER_RATE)
log.v("ARTICLES_CLUSTER_ID:", ARTICLES_CLUSTER_ID)


def main():
    articles_dir = ARTICLES_DIR
    base_dir = "./covid-19-news-articles/process-07_sentences-cluster/"

    embeds_pdist_dir = base_dir + \
        "process-07_sentences-cluster_embeds-pdist.txt"
    dest_dir = base_dir + \
        "process-07_sentences-cluster_reduced-data-to-" + \
        str(REDUCED_NUM) + '/' + \
        "process-07_sentences-cluster.txt"
    dendrogram_dir = base_dir + \
        "process-07_sentences-cluster_dendrogram.png"
    color_dendrogram_dir = base_dir + \
        "process-07_sentences-cluster_color_dendrogram.png"
    result_dir = base_dir + \
        "process-07_sentences-cluster_result.csv"
    threshold_dependencies_dir = base_dir + \
        "process-07_sentences-cluster_threshold-dependencies.png"
    num_of_cluster_dir = base_dir + \
        "process-07_sentences-cluster_num_of_cluster.png"
    silhouette_coefficient_dir = base_dir + \
        "process-07_sentences-cluster_num-of-clusters-dependency-on-silhouette-coefficient.png"
    exe_time_dir = "./covid-19-news-articles/archive/exe-time/exe-time_process_07_sentences_cluster_generator.txt"

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

    log.v("do_debug:", do_debug)
    log.v("reduce_data:", reduce_data)

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
    # nation-n;article-n;sentence-id;c;feature-x;feature-y;c-embedding;sent-1#...\n
    article_info_or_sentences = []

    with open(articles_dir, "r", encoding="utf_8") as f:
        article_info_or_sentences = f.readlines()
        log.v("articles:")
        log.v("article_info_or_sentences[0]:", article_info_or_sentences[0])
        log.v("article_info_or_sentences[1]:", article_info_or_sentences[1])
        log.v("article_info_or_sentences[2]:", article_info_or_sentences[2])
        log.v()

    ##################################################
    log.d("*** extract nation id, article id, c-sentence-id & claim sentence embeddings ***")
    log.d("*** & save lines by each claim sentences ***")
    ##################################################
    nation_article_claim_ids = []  # ["IN;n;sentence-id(claim)"]
    claim_lines = []  # [[lines each articles], ...]
    claim_embeds = []  # [[2.50864863e-01, 9.60696563e-02, ...], ...]
    NATION_ID_IDX = 0
    ARTICLE_ID_IDX = 1
    CLAIM_SENTENCE_ID_IDX = 2
    EMBED_IDX = 6

    # nation-n;article-n;[e-embedding]
    # nation-n;article-n;sentence-id;c;feature-x;feature-y;c-embedding;sent-1#...\n
    for article_info_or_sentence in article_info_or_sentences:

        splits_with_semicolon = article_info_or_sentence.split(';')
        len_splits_with_semicolon = len(splits_with_semicolon)

        # article or evidence sentence info
        if len_splits_with_semicolon == 3 or len_splits_with_semicolon == 7:
            pass

        # claim sentence info
        elif len_splits_with_semicolon == 8:
            # extract nation_article_claim_ids
            nation_id = str(splits_with_semicolon[NATION_ID_IDX])
            article_idx = str(splits_with_semicolon[ARTICLE_ID_IDX])
            claim_idx = str(
                splits_with_semicolon[CLAIM_SENTENCE_ID_IDX])
            ids = ';'.join([nation_id, article_idx, claim_idx])
            nation_article_claim_ids.append(ids)

            # extract lines by each claim sentences
            claim_lines.append(article_info_or_sentence)

            # extract sentence_embeds
            claim_embed_str = splits_with_semicolon[EMBED_IDX]
            claim_embed_strs = claim_embed_str.strip().split()
            claim_embed = [float(embed_str)
                           for embed_str in claim_embed_strs]
            claim_embeds.append(claim_embed)
        # error
        else:
            log.e(
                "unsuspected len_splits_with_semicolon: ",
                len_splits_with_semicolon)
            exit()

    if nation_article_claim_ids == []:
        log.w("no claim exist")
        exit()

    log.v("nation_article_claim_ids[0]: ", nation_article_claim_ids[0])
    log.v("claim_embeds[0]: ", claim_embeds[0])
    log.v("claim_lines[0]: ", claim_lines[0])
    log.v("claim_lines[-1]: ", claim_lines[-1])
    log.v()

    # reduce data num (because of memory size error)
    # if reduce_data:
    #     shuffle_idxs = list(range(len(nation_and_article_ids)))
    #     random.seed(RANDOM_SEED)
    #     random.shuffle(shuffle_idxs)
    #     nation_and_article_ids = [
    #         nation_and_article_ids[i] for i in shuffle_idxs[:REDUCED_NUM]]
    #     article_embeds = [article_embeds[i]
    #                       for i in shuffle_idxs[:REDUCED_NUM]]
    #     articles_lines = [articles_lines[i]
    #                       for i in shuffle_idxs[:REDUCED_NUM]]
    #     log.v("nation_and_article_ids[:10]: ",
    #           nation_and_article_ids[:(10 % REDUCED_NUM)])
    #     log.v("article_embeds[0]: ", article_embeds[0])
    #     log.v("articles_lines[0]: ", articles_lines[0])
    #     log.v()

    ##################################################
    log.d("*** clustering (substitute claim_embeds) ***")
    ##################################################

    # time mesurement: start
    clustering_start_time = time.time()

    # exe
    embeds_pdist = pdist(claim_embeds, metric=METRIC)
    clustering_result = linkage(embeds_pdist, method=METHOD)
    # clustering_result = linkage(claim_embeds, metric=METRIC, method=METHOD)

    # print time
    clustering_time = time.time() - clustering_start_time
    log.d("clustering time (sec):", clustering_time)

    # save embed pdist
    with open(embeds_pdist_dir, "w+", encoding="utf_8") as f:
        embeds_pdist_2_str = [str(p) for p in embeds_pdist]
        f.write("\n".join(embeds_pdist_2_str))

    # debug
    embeds_square_form = squareform(embeds_pdist)
    log.v("clustering_result[0]:", clustering_result[0])
    log.v("len(clustering_result):", len(clustering_result))
    log.v("embeds_pdist[0]:", embeds_pdist[0])
    log.v("embeds_square_form[0]:", embeds_square_form[0])
    log.v("embeds_square_form[1]:", embeds_square_form[1])
    log.v("embeds_square_form[2]:", embeds_square_form[2])

    ##################################################
    log.d("*** print clustering result ***")
    ##################################################
    result_df = pd.DataFrame(clustering_result)
    result_df.to_csv(result_dir)

    if do_debug:
        log.v("result_df:", result_df)
    log.v("result_df[0][0] (1st node      ) :", result_df[0][0])
    log.v("result_df[1][0] (2nd node      ) :", result_df[1][0])
    log.v("result_df[2][0] (nodes distance) :", result_df[2][0])
    log.v("result_df[3][0] (cluster size  ) :", result_df[3][0])

    ##################################################
    log.d("*** draw num of clusters dependency on silhouette coefficient ***")
    log.d("*** & calc best them ***")
    ##################################################
    # time mesurement: start
    drawing_num_and_silhouette_start_time = time.time()

    # distance_matrix = get_distance_matrix(result_df)
    distance_matrix = embeds_square_form
    best_num_of_cluster = 0
    best_cluster_by_number = []
    best_silhouette_coefficient = -100100100
    # max_num_of_cluster = REDUCED_NUM * MAX_NUM_OF_CLUSTER_RATE
    max_num_of_cluster = len(nation_article_claim_ids) * \
        MAX_NUM_OF_CLUSTER_RATE
    x = []
    y = []
    for num_of_cluster in range(2, len(result_df)):
        cluster_by_number = get_cluster_by_number(
            clustering_result, num_of_cluster)
        silhouette_coefficient = silhouette_coefficient2(
            cluster_by_number, distance_matrix)
        # if silhouette_coefficient > max_silhouette_coefficient:
        if silhouette_coefficient > best_silhouette_coefficient and num_of_cluster <= max_num_of_cluster:
            best_num_of_cluster = num_of_cluster
            best_cluster_by_number = cluster_by_number
            best_silhouette_coefficient = silhouette_coefficient
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

    log.d("len(nation_article_claim_ids): ", len(nation_article_claim_ids))
    log.d("max_num_of_cluster: ", max_num_of_cluster)
    log.d("best_num_of_cluster: ", best_num_of_cluster)
    log.d("max_silhouette_coefficient: ", best_silhouette_coefficient)
    log.v("best_cluster_by_number: ", best_cluster_by_number)
    log.v()

    ##################################################
    log.d("*** draw threshold dependency ***")
    ##################################################
    # time mesurement: start
    drawing_threshold_dependency_start_time = time.time()

    # exe
    best_threshold = draw_threshold_dependency(
        clustering_result,
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

    id_labels = nation_article_claim_ids if DRAW_IDS else [
        ''] * len(nation_article_claim_ids)

    # exe
    # dendrogram_fig = plt.figure(figsize=(14.4, 19.2))
    # dendrogram_fig = plt.figure(figsize=(19.2, 14.4))
    dendrogram_fig = plt.figure(figsize=(19.2, 7.2))
    dendrogram(
        clustering_result,
        orientation='right',
        labels=id_labels,
        color_threshold=0.0
    )
    # plt.title(
    #     "Article Dendrogram by Evidence Sentences",
    #     fontsize=TITLE_SIZE - 6)
    plt.xlabel("Distance between Clusters", fontsize=LABEL_TITLE_SIZE)
    plt.ylabel("Claim Sentence ID", fontsize=LABEL_TITLE_SIZE)
    plt.grid()
    plt.tick_params(labelsize=LABEL_SIZE / 2)
    # plt.show()
    dendrogram_fig.savefig(dendrogram_dir)

    # exe color ver

    # set color
    # @see https://www.webdevqa.jp.net/ja/python/python%EF%BC%88linkcolorfunc%EF%BC%9F%EF%BC%89%E3%81%AEscipy%E6%A8%B9%E7%8A%B6%E5%9B%B3%E3%81%AE%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%A0%E3%82%AF%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC%E3%82%AB%E3%83%A9%E3%83%BC/825416841/
    # cmap = cm.Rainbow(np.linspace(0, 1, best_num_of_cluster))
    # link_cols = [mpl.colors.rgb2hex(rgb[:3]) for rgb in cmap]

    # color_dendrogram_fig = plt.figure(figsize=(14.4, 19.2))
    # color_dendrogram_fig = plt.figure(figsize=(19.2, 14.4))
    color_dendrogram_fig = plt.figure(figsize=(19.2, 7.2))
    dendrogram(
        clustering_result,
        orientation='right',
        labels=id_labels,
        color_threshold=best_threshold,
        # link_color_func=lambda x: link_cols[x]
    )
    # plt.title(
    #     "Article Dendrogram by Evidence Sentences",
    #     fontsize=TITLE_SIZE - 6)
    plt.xlabel("Distance between Clusters", fontsize=LABEL_TITLE_SIZE)
    plt.ylabel("Claim Sentence ID", fontsize=LABEL_TITLE_SIZE)
    plt.grid()
    plt.tick_params(labelsize=LABEL_SIZE / 2)
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
    plt.ylabel("Num of Claim Sentences", fontsize=LABEL_TITLE_SIZE)
    plt.tick_params(labelsize=LABEL_SIZE)
    plt.grid()
    num_of_cluster_fig.savefig(num_of_cluster_dir)

    ##################################################
    log.d("*** save lines in each cluster with best_cluster_by_number ***")
    ##################################################
    # [["(claim line 1 of cluster 1 including \n)(claim line 2 of cluster 1 including \n)..."], ...]
    clusters_claims = [''] * best_num_of_cluster
    for claim_idx, cluster_id in enumerate(best_cluster_by_number):
        claim_line = claim_lines[claim_idx]
        clusters_claims[cluster_id] += claim_line

    # write
    for _, cluster_id in enumerate(best_cluster_by_number):
        dest_dir_each_cluster_id = re.sub(
            "\\.txt", "_" + str(cluster_id) + ".txt", dest_dir)
        with open(dest_dir_each_cluster_id, "w+", encoding="utf_8") as f:
            f.write(clusters_claims[cluster_id])

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
    n_clusters = len(result) + 1
    n_samples = len(result) + 1
    # df1 = pd.DataFrame(result)
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    best_threshold = 0.0

    # get distances of each connection from result
    for i in range(len(result)):
        # n1 = int(result[i][0])
        # n2 = int(result[i][1])
        distasnce = result[i][2]
        if n_clusters == best_num_of_cluster:
            best_threshold = distasnce
        x1.append(distasnce)  # threshold
        x2.append(distasnce)  # threshold
        y1.append(n_clusters)
        y2.append(float(n_samples) / float(n_clusters))
        n_clusters -= 1

    # draw
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
    # plt.xlabel('Threshold', fontsize=LABEL_TITLE_SIZE)
    plt.xlabel('Distance between Clusters', fontsize=LABEL_TITLE_SIZE)
    plt.ylabel('Average of Cluster Size', fontsize=LABEL_TITLE_SIZE)
    plt.grid()
    plt.tick_params(labelsize=LABEL_SIZE)
    # plt.show()
    dependencies_fig.savefig(threshold_dependencies_dir)

    # for finding best clustering
    return best_threshold


# get cluster = [class(sentence idx), ...] from num of clusters
def get_cluster_by_number(result, num_clusters):
    output_clusters = []
    num_connect, _ = result.shape
    current_num_clusters = num_connect + 1
    current_cluster_id = num_connect + 1
    father_of = {}

    for i in range(len(result) - 1):
        node_1_idx = int(result[i][0])
        node_2_id = int(result[i][1])
        # distance = result[i][2]
        current_num_clusters -= 1
        if current_num_clusters >= num_clusters:
            father_of[node_1_idx] = current_cluster_id
            father_of[node_2_id] = current_cluster_id

        current_cluster_id += 1

    cluster_dict = {}
    for connect_idx in range(num_connect + 1):
        if connect_idx not in father_of:
            output_clusters.append([connect_idx])
            continue

        node_2_id = connect_idx
        m = False
        while node_2_id in father_of:
            m = father_of[node_2_id]
            #print [n2, m]
            node_2_id = m

        if m not in cluster_dict:
            cluster_dict.update({m: []})
        cluster_dict[m].append(connect_idx)

    output_clusters += cluster_dict.values()

    output_cluster_id = 0
    output_cluster_ids = [0] * (num_connect + 1)
    for cluster in sorted(output_clusters):
        for i in cluster:
            output_cluster_ids[i] = output_cluster_id
        output_cluster_id += 1

    return output_cluster_ids


# def get_distance_matrix(df):
#     distance_matrix = []
#     for i in range(len(df)):
#         vec1 = df.iloc[i, :].values
#         distance_array = []
#         # log.v("vec1", vec1)
#         for j in range(len(df)):
#             vec2 = df.iloc[j, :].values
#             dist = 0.
#             for v1, v2 in zip(vec1, vec2):
#                 # log.v("v1", v1)

#                 dist += (v1 - v2) ** 2
#             distance_array.append(math.sqrt(dist))
#         distance_matrix.append(distance_array)
#     return distance_matrix


def silhouette_coefficient2(clusters, distance_matrix):
    do_debug = False
    if do_debug:
        log.v("clusters:", clusters)
        log.v("distance_matrix:", distance_matrix)
        log.v("len(clusters):", len(clusters))
        log.v("len(distance_matrix):", len(distance_matrix))
        log.v("clusters[0]:", clusters[0])
        log.v("distance_matrix[0]:", distance_matrix[0])

    num_clusters = max(clusters) + 1
    same_clusters_dists = [[] for _ in range(num_clusters)]
    diff_clusters_dists = [[[] for two in range(num_clusters)]
                           for one in range(num_clusters)]

    for sentence_id_1, cluster_id_1 in enumerate(clusters):
        for sentence_id_2, cluster_id_2 in enumerate(clusters):

            # see triangular mat
            if sentence_id_1 < sentence_id_2:
                # log.v("i, k:", i, k)
                # get same & different classes' samples' distance from distance
                # mat
                dist = distance_matrix[sentence_id_1][sentence_id_2]
                if cluster_id_1 == cluster_id_2:  # same cluster
                    same_clusters_dists[cluster_id_1].append(dist)
                else:  # different cluster
                    diff_clusters_dists[cluster_id_1][cluster_id_2].append(
                        dist)

    # log.v("same_clusters_dists", same_clusters_dists)
    # log.v("diff_clusters_dists", diff_clusters_dists)

    silhouette_coefficients = []

    # calc silhouette_coefficient about each clusters
    for cluster_id_1 in range(num_clusters):
        a = 0
        b = 0

        if same_clusters_dists[cluster_id_1] == []:
            # num of cluster member = 1
            # pass # (b+0)/b=1
            continue
        else:
            a = sum(same_clusters_dists[cluster_id_1]) / \
                len(same_clusters_dists[cluster_id_1])

        aves_diffs_clusters_dists = []
        for cluster_id_2 in range(num_clusters):
            if cluster_id_1 == cluster_id_2:
                continue

            current_diffs_clusters_dists = diff_clusters_dists[cluster_id_1][cluster_id_2]
            current_diffs_clusters_dists += diff_clusters_dists[cluster_id_2][cluster_id_1]

            current_ave = 0
            if current_diffs_clusters_dists == []:
                # num of cluster = 1
                # pass
                continue
            else:
                current_ave = sum(current_diffs_clusters_dists) / \
                    len(current_diffs_clusters_dists)
            aves_diffs_clusters_dists.append(current_ave)

        b = min(aves_diffs_clusters_dists)

        # log.v("a", a)
        # log.v("b", b)
        # log.v("aves_diffs_clusters_dists:", aves_diffs_clusters_dists)

        silhouette_coefficients.append((b - a) / max(b, a))

    # calc silhouette coefficient
    return sum(silhouette_coefficients) / len(silhouette_coefficients)


if __name__ == "__main__":
    main()