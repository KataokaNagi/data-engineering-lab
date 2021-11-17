<!-- tex script for md -->
<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
<script type="text/x-mathjax-config">
 MathJax.Hub.Config({
 tex2jax: {
 inlineMath: [['$', '$'] ],
 displayMath: [ ['$$','$$'], ["\\[","\\]"] ]
 }
 });
</script>

# 週次報告書 2021年11月17日
AL18036 片岡 凪

## 1. 今回の報告会までに実施する予定だったこと
- 区切り文字に!と?を考慮
- Stanzaの公式ドキュメントの読み込み
- 文章分割の実装
- ~~EvidenceとClaimの分類~~
- ~~クラスタリングの実装~~

## 2. 実施内容

### 概要
文章分割の実装まで行ったが、その実行速度に問題が発生している。
また、寄り道をしすぎて今週も分類まで行うことができなかった。
実装は楽しいが、寄り道をしすぎないように研究を進めていきたい。

### 目次
- 2.1 samba, venvの調査
- 2.2 区切り文字に!と?を考慮
- 2.3 Stanzaの公式ドキュメントの読み込み
- 2.4 文章分割の実装
- 2.5 ubuntu, bash, python, gitの寄り道

<!-- ![](img/)
<div style="text-align: center;">
図. 
</div>
<br>
<br> -->

### 2.1 samba, venvの調査
**sambaについて調査**し、**東京サーバー**の2021年度フォルダで容易に**同様なことができる**ことがわかった。
また、**venv**について調査し、bashで自動化した。
venv外の環境とは別に、毎回ライブラリのpathを通す必要があることに注意したい。
<!-- しかし、activateしてもライブラリが上手く利用できず、venvを使わなければ実行できたため、暫くはvenvを使わないで実行することとした。
環境が複雑になり、venvが必要となったときに詳しく再調査する予定である。
-> pathを通せば上手く動いた -->

### 2.2 区切り文字に!と?を考慮
置換処理に用いるの句読点として、「.」 とは別に **「!」 と 「?」 を追加**した。
該当のコードは以下の通りで、容易に実装できた。
```
print_debug("rm other than alphabets, numbers, spaces, punctuations")
gsub(/[^a-z0-9 \.!?]/,"")

# rm punctuations & spaces
print_debug("rm spaces before periods")
gsub(/ +\./,".")
print_debug("rm spaces before exclamation marks")
gsub(/ +!/,"!")
print_debug("rm spaces before question marks")
gsub(/ +\?/,"?")

print_debug("multi periods -> single period")
gsub(/\.{2,}/,".")
print_debug("multi exclamation marks -> single exclamation mark")
gsub(/!{2,}/,"!")
print_debug("multi question marks -> single question mark")
gsub(/\?{2,}/,"?")    

print_debug("rm periods at beginning of line")
gsub(/^\.+/,"")
print_debug("rm exclamation marks at beginning of line")
gsub(/^!+/,"")
print_debug("rm question marks at beginning of line")
gsub(/^\?+/,"")
```

加えて、**gawkではなくmawkで処理**するようにbashを書き換えた。

また、デバッグの際、**tolowerが一部の文字列に作用していないことが発覚**した。
これに対し、以下の**エラー修正**を行った。
```
# 修正前
gsub(/*./, tolower($0)) # 「全ての文字列」ではなく「改行以外の文字列の0個以上の連続」の検索

# 修正後
$0 = tolower($0)
```

### 2.3 Stanzaの公式ドキュメントの読み込み
[Stanzaの公式ドキュメント](https://stanfordnlp.github.io/stanza/)の研究に必要な項目を読み込んだ。

Stanzaは、モデルとして**UDモデル**（UD treebank）を利用している。
このモデルは単語同士の依存関係木を構築する国際プロジェクトとして作成されている。
また、モデル著作権とライセンスが不明確であるが、基本的にはライセンス「[Open Data Commons Attribution License v1.0](https://opendatacommons.org/licenses/by/1-0/)」に準拠するものであるとの記載があった。
このライセンスでは、ライセンス表示をすれば**自由な利用が可能**である。

また、モデルに利用する英文データは4つあり、うち**ewt package**が**最大のデータで学習**されており、デフォルトで設定されている。
ライセンスは[Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) ](https://creativecommons.org/licenses/by-sa/4.0/)であり、同じライセンスを付与して**自由に利用が可能**である。
しかし、CoNLL 2018 UD shared task official evaluation scriptによる文章分割の**評価スコア**を参照すると、ewt packageが81.13/100であるのに対し、**arTuT packageは100/100でより高い**。
本研究で用いるデータとしてどちらが最適であるか、**余裕があれば試してみる価値がある**。

さらに、**大量のデータ**を扱う際には**StanzaではなくルールベースのspaCyを用いるべきだ**との記載があった。
spaCyのアルゴリズムはStanzaに組み込まれているため、以下のように容易に切り替えることができる。

```
# use stanza
nlp = stanza.Pipeline(lang="en", processors=tokenize)

# use spaCy
nlp = stanza.Pipeline(lang="en", processors={'tokenize': 'spacy'})
```

両方のアルゴリズムで実行し、**省略のピリオドの分割精度**と**実行速度**を比較する予定である。
分割精度は、LibbreOfficeを扱う際に使用した以下のような正規表現を用いて、それぞれ**30件ほど手動で確認**する予定である。
```
\w\.\w\.\w.
\w\.\w.
[A-Z][a-z]\.
```

### 2.4 文章分割の実装
以下のように文章分割を実装した。
ソースコードは難しくなく、特筆すべきことはなかった。

```
import sys
import argparse
import time
import stanza
stanza.download('en')

# option
use_spacy = True
use_stanza = not use_spacy
do_debug = False
num_debug = 10

# consts of dir
DATASET_DIRS = [
    "./covid-19-news-articles/India-Articles_preprocess_02_awk.txt",
    "./covid-19-news-articles/Japan-Articles_preprocess_02_awk.txt",
    "./covid-19-news-articles/Korea-Articles_preprocess_02_awk.txt"
    # "./covid-19-news-articles/UK-Articles_preprocess_02_awk.txt"
]
DIST_DIRS = [
    "./covid-19-news-articles/India-Articles_preprocess_03_spilt-sentences.tsv",
    "./covid-19-news-articles/Japan-Articles_preprocess_03_spilt-sentences.tsv",
    "./covid-19-news-articles/Korea-Articles_preprocess_03_spilt-sentences.tsv"
    # "./covid-19-news-articles/UK-Articles_preprocess_03_spilt-sentences.tsv"
]

# debug option
arg_parser = argparse.ArgumentParser(description='-d: debug')
arg_parser.add_argument("-d", "--debug", help="optional debug", action="store_true")
arg_parser.add_argument("--spacy", help="optional debug", action="store_true")
arg_parser.add_argument("--stanza", help="optional debug", action="store_true")
arg = arg_parser.parse_args()
do_debug = arg.debug
if arg.stanza:
    use_spacy = False
    use_stanza = True
if arg.spacy:
    use_spacy = True
    use_stanza = False

# time mesurement: start
start_time = time.time()

# open dataset
for dir_idx in range(len(DATASET_DIRS)):
    with open(DATASET_DIRS[dir_idx], 'r') as fi, open(DIST_DIRS[dir_idx], 'a+') as fw:
        num_line = 0
        for line in fi:
            # split sentences
            processors = \
                'tokenize' if use_stanza \
                else \
                {'tokenize': 'spacy'} if use_spacy \
                else \
                print("unsuspected processors", file=sys.stderr)
            nlp = stanza.Pipeline(lang="en", processors=processors)
            doc = nlp(line)
            spilit_sentences = [sentence.text for sentence in doc.sentences]
            spilit_sentences = "#".join(spilit_sentences)
            
            # write
            fw.write(spilit_sentences)
            
            # debug
            if do_debug:
                print("num_line:", num_line, spilit_sentences)
                if ++num_line == num_debug:
                    break

# print time
print(time.time() - start_time)
```

実行にあたり、以下のように**pipとpip3が混合していることを少し不安視している**。
```
pip3 install cython

pip install -U pip setuptools wheel
pip install -U spacy

pip3 install stanza
```

pip3を用いた以下のコマンドはエラーとなる。
記憶によると「pip3 setuptools wheelが存在しない」と出力されてしまう。
```
pip3 install -U pip3 setuptools wheel
```

プログラムを実行したところ、**stanzaより高速なspacyのアルゴリズムでも1記事あたり5分ほどかかり、1記事目でフリーズしてしまった**。
設定次第で**gpu**を用いることができるため、**研究室に赴いてセットアップ**を行うことを検討している。
また、**Stanzaに似たツールであるUD-Pipeの使用**や、**簡単な正規表現と文の長さによる外れ値除去**を検討している。

### 2.5 ubuntu, bash, python, gitの寄り道
ubuntu上で快適に作業するため、**仮想デスクトップ**と**タスクバー**に関して調査し、改善する設定を行った。

また、今後のプログラムの自動化を効率化や環境構築の記録のため、**bashについて更に学習**した。
学習内容に基づき、より動的に実行できるように既存のbashファイルを編集した。
具体的には、dir名の共通項を変数に変えて見通しを良くしたり、getopts()によるオプション解析を行ったりした。

また、**pythonプログラムの高速化とオプション解析**に関して調査した。
調査内容に基づき、文字列連結に += ではなく ''.join() を用いる、オプション解析にargparseを用いるなどといった工夫を行った。

ubuntu上で`git push`を行った際、`Gitリモートに対して認証できませんでした`といったエラーが発生した。
エラーに対し、**SSH Key**をGithubに登録し、**ユーザ名やメールアドレスを再登録**するなどを試みたが、解決には至らなかった。
引き続き調査・改善に努めたい。
改善案として、**WindowsのVSCodeからSSH接続**し、Windowsから`git push`することを考えている。
ツールとしては、VSCodeのRemote SSHを使用する予定である。

## 3. 次回までに実施予定であること
- 文章分割のライブラリ関係のエラーを除去
- git pushのエラーを除去
    - VSCodeでSSH接続
- EvidenceとClaimの分類
- クラスタリングの実装
<!-- - venvのpath設定の自動化 -->

## 4. メモ
- 報告会の振り返り
    - venv
        - https://qiita.com/fiftystorm36/items/b2fd47cf32c7694adc2e
        - venv.bashの作成
        - git ignore
            - venvフォルダ
            - csv
    - samba
        - Tokyoサーバー使えば不要
- ubuntuの環境構築
    - 仮想デスクトップ
        - 3つ以上の同時押しができてないっぽい
            - 固定キーの設定で可能
            - キーマップの変更
                - CompizConfig Setting Manager
                - https://forums.ubuntulinux.jp/viewtopic.php?id=19231
    - タスクバー
        - ubuntu dock
        - https://qiita.com/Shunmo17/items/3afc05bc49b29af54c05
            - アクティビティ > 検索ワードを入力 > Tweaaks > 拡張機能
- シェルの勉強
    - https://www.tohoho-web.com/ex/shell.html
- !?の置換の対応
    - ?のエスケープに注意
- gawk -> mawk
- tolowerでlowerになっていない文字列があった
    - URL
    - COVID
    - https://teratail.com/questions/131228
        -  .* は「全ての文字列」ではなくて「改行以外の文字列の0個以上の連続」になる
        -  [\s\S]でいけるらしい
        - mawkではセグメンテーションフォールト
    - https://teratail.com/questions/131228
        - $0=tolower($0)で解決
- awk用のbashのクリーン
    - dir名を動的に
    - オプション解析
        - https://t.co/46CkKLi5UH?amp=1
        - getoptsとwhile, caseとshift
- Stanzaの公式ドキュメント
    - https://stanfordnlp.github.io/stanza/
    - Available Models & Languages
        - UDモデル（UD treebank）を利用
            - 依存関係木の国際プロジェクト
            - 何で学習しているかは不明
                - https://en.wikipedia.org/wiki/Universal_Dependencies
        - モデルの著作権とライセンスは不明確
            - [Open Data Commons Attribution License v1.0](https://opendatacommons.org/licenses/by/1-0/)
                - 要ライセンス表示
        - ewt packageがデフォルト
            - 最大のデータで学習された
            - [Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) ](https://creativecommons.org/licenses/by-sa/4.0/)
                - 再配布可能
                - 同じライセンスで配布
                - 追加的な制限は不可
                - Sentencesスコアが81.13
                    - CoNLL 2018 UD shared task official evaluation script
                    - partutは100
                        - こちらの方が良いのでは？
    - Tokenization & Sentence Segmentation
        - Options
            - tokenize_batch_size
                - メモリ（メイン or GPU）が必要だが速くなる
            - tokenize_pretokenized
                - デフォルトのオフのままでよい
                - 改行で文が分割されると仮定
    - Use spaCy for Fast Tokenization and Sentence Segmentation
        - 大量のNLPにはspaCyによるトークナイザーを推奨
            - ルールベースで高速
            - processors={'tokenize': 'spacy'}とするだけ
                - spaCyでトークン化、Stanzaでアノテーション
            - 両方試して処理速度と省略のピリオドの分割精度を見る
- 文章分割
    - pythonの高速化
        - pythonの速度で気にするところ(高速化メモ) - nobUnagaの日記 https://nobunaga.hatenablog.jp/entry/2018/03/19/081425 
            - appendよりも[None]*n_sizeで最初に領域確保
            - 文字列連結は+=よりも''.join()
            - グローバル変数よりもmain()内ローカル変数
            - t=x, x=y, y=t よりも x, y=y,x
            - 可能ならhashのset
            - 正規表現よりもfind, in
        - Python で AtCoder をするあれこれ https://qiita.com/c-yan/items/dbf2838cdd89864ef5ac #Qiita
            - グローバル変数はhash、ローカル変数は配列の速度
            - 文字列連結は+=がO(N^2) 、リストにappendして join すると O(NlogN)
            - pythonは加減乗除もビット演算も総じて遅く、CPUのパイプライン予測の乱れを鑑みてもif文の方が速い？
        - Rubyのハッシュと配列の検索速度の違い https://kiyotakakubo.hatenablog.com/entry/20110725/1311597106 
            - 検索はarrayよりhashがかなり速い
            - 場所がわかっていればarrayの方が少し速い
            - hashは作成が遅い
    - オプション解析
        - argparse
            - https://blog.denet.co.jp/python-command/
            - arg_parser = argparse.ArgumentParser(description='-d: debug')
            - arg_parser.add_argument("-d", "--debug", help="optional debug", action="store_true")
            - arg = arg_parser.parse_args()
            - do_debug = arg.debug
    - (ModuleNotFoundError解決方法)[https://qiita.com/homines22/items/c43e564811466bf088e7]
        - echo 'export PYTHONPATH="$PYTHONPATH:/home/test/lib"' >> ~/.bashrc
        - python3にするのを忘れずに
    - pip3 install
        - pip3 install cython
- gitのubuntu設定
    - [](https://qiita.com/majka/items/aba924de8d4a92f75dbb)