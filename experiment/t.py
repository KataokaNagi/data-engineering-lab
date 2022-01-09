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

s = "  "
print("left", s.strip(), "right")
