import re

DIST_DIRS = [
    "./covid-19-news-articles/india-articles_preprocess_03_spilt-sentences.txt",
    "./covid-19-news-articles/japan-articles_preprocess_03_spilt-sentences.txt",
    "./covid-19-news-articles/korea-articles_preprocess_03_spilt-sentences.txt"
    # "./covid-19-news-articles/uk-articles_preprocess_03_spilt-sentences.txt"
]

do_debug = True
use_spacy = False
use_stanza = True

# edit DIST_SIRS according to options
for i, dir in enumerate(DIST_DIRS):
    if use_spacy:
        DIST_DIRS[i] = re.sub("\.txt","_with-spacy.txt", dir)
    if use_stanza:
        DIST_DIRS[i] = re.sub("\.txt","_with-stanza.txt", dir)
        print("use stanza")

    if do_debug:
        DIST_DIRS[i] = re.sub("\.txt","_debug.txt", dir)
    # print(dir)
    print(DIST_DIRS[i])

for dir in DIST_DIRS:
    print(dir)
