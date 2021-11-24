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

# 週次報告書 2021年11月24日
AL18036 片岡 凪

## 1. 今回の報告会までに実施する予定だったこと
- 文章分割のライブラリ関係のエラーを除去
- git pushのエラーを除去
    - VSCodeでSSH接続
- ~~EvidenceとClaimの分類~~
- ~~クラスタリングの実装~~
<!-- - venvのpath設定の自動化 -->

## 2. 実施内容

### 概要
GPUの増設、設定と文章分割を完了した。

### 目次
- 2.1 venvやgitの環境調整（skip）
- 2.2 RTX3070で学習、GT710で映像出力（後者は断念）
- 2.3 StanzaとspaCyによる文章分割の修正と比較

### 2.1 venvやgitの環境調整（skip）
pythonライブラリの実行のため、venvのactivateにpathを通すシェルスクリプトを追記した[1]。  


また、Ubuntu上で`git push`ができないエラーを解決するため、WindowsのVScodeからSSH接続する設定を行った[2]。  
  
[1] [How do you set your pythonpath in an already-created virtualenv?](https://stackoverflow.com/questions/4757178/how-do-you-set-your-pythonpath-in-an-already-created-virtualenv)  
[2] [Visual Studio CodeでLinux ホストリモート開発](https://qiita.com/whim0321/items/ae72b2dd5fd41beaef04)

<!-- ![](img/)
<div style="text-align: center;">
図. 
</div>
<br>
<br> -->

### 2.2 RTX3070で学習、GT710で映像出力（後者は断念）
StanzaでGPUを利用するため、研究室に赴いてRTX3070を増設した。
増設直後はPC起動時に
```
started gnome display manager
```
の項目で止まってしまい、デスクトップに入ることができなかったが、SSH接続したCUIで
```
sudo ubuntu-drivers autoinstall
```
を実行することで解決することができた。

続いて、PC資源の有効活用のため、RTX3070で学習し、GT710で映像出力できる設定について調査した。
映像出力するGPUを変更するためには、以下のコマンドで作成した設定ファイルにGPUのIDを追記すればよい[3]。
```
sudo nvidia-xconfig
```
  
[3] [GPUボードが複数ある Ubuntu 20.04でディスプレイ出力に使うGPUを指定したい](https://ja.stackoverflow.com/questions/74811/gpu%E3%83%9C%E3%83%BC%E3%83%89%E3%81%8C%E8%A4%87%E6%95%B0%E3%81%82%E3%82%8B-ubuntu-20-04%E3%81%A7%E3%83%87%E3%82%A3%E3%82%B9%E3%83%97%E3%83%AC%E3%82%A4%E5%87%BA%E5%8A%9B%E3%81%AB%E4%BD%BF%E3%81%86gpu%E3%82%92%E6%8C%87%E5%AE%9A%E3%81%97%E3%81%9F%E3%81%84)

しかし、GPUのIDを確認するために以下のようなコマンドを実行したが、GT710を認識することができなかった[3][4][5]。
```
sudo update-pciids # 型番情報のアップデート
lspci | grep VGA # 表示方法1
lspci | grep -i nvidia # 表示方法2
nvidia-smi # 表示方法3
```

[4] [Ubuntu 18.04 で、NVIDIAのリポジトリを利用してtensorflow-gpu環境を構築するシンプルな方法](https://www.nemotos.net/?p=3176)  
[5] [Linuxでコマンドラインからマシンスペックを確認する方法](https://qiita.com/DaisukeMiyamoto/items/98ef077ddf44b5727c29)


原因として適したGPUドライバがインストールされていない可能性があるため、ドライバのための以下のコマンドを入力して再びIDを確認したが、解決には至らなかった[6]。
```
ubuntu-drivers decices # 推奨ドライバの確認
ubuntu-drivers autoinstall # 再びオートインストール
sudo add-apt-repository ppa:graphics-drivers/ppa # ドライバのリストの更新
sudo apt install nvidia-driver-495 # 推奨ドライバのインストール
```

[6] [UbuntuにNVIDIA driverをインストール/再インストールする方法](https://qiita.com/yto1292/items/463e054943f3076f36cc)

次に、TFが実行できるまで環境構築を行うことで、映像出力するGPU設定も間接的に解決しないかと考えた。
`3070 tensorflow` `3070 tensorflow docker`などで検索したが、定番の構築方法はなく、「よくわからないけどこれで動いた」といった情報が多かった。
検索トップの記事の多くは5カ月以上前のもので、種々のツールのバージョンの不対応に関して試行錯誤しているようだった。

そこで、まず3070に限らない定番の手法で環境構築を行うことを考えた。
志田くんの資料を参考にnvidia-driver, CUDA, cuDNN, tensorflowをインストールした。
志田くんの資料ではtensorflow-gpuをインストールしていたが、公式ドキュメントによるとtensorflowの方が新しいらしい[7]。
以下のようにTFの実行し、テンソルが変えることを確認した。

```
# コマンド
python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

# 実行結果
（中略）
tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
（このTensorFlowバイナリは、oneAPI Deep Neural Network Library（oneDNN）で最適化されており、パフォーマンスが重視される操作では以下のCPU命令を使用します。 AVX2 FMA その他の処理でこれらの命令を有効にするには、適切なコンパイラフラグでTensorFlowを再構築します。）
（中略）
tensorflow/core/common_runtime/gpu/gpu_device.cc:1510] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 6033 MB memory:  -> device: 0, name: NVIDIA GeForce RTX 3070, pci bus id: 0000:01:00.0, compute capability: 8.6 tf.Tensor(-1670.4432, shape=(), dtype=float32)```
```

[7] [pip での TensorFlow のインストール](https://www.tensorflow.org/install/pip?hl=ja)

TFは実行できたが、GT710が認識されることはなかった。
残る原因としては、PCIスロットの接触不良や、挿すスロットのミスなどの物理的要因が考えられる。
似た問題として、M.2 SSDを挿したときに電力だかクロック周波数だかの問題で他のPCIレーンの出力が落ちることがある。
現在、CPUに近いPCIスロットから順にRTX3070, GT710を接続している。

学習と映像出力を分けた理想のGPU構成にはなっていないが、TFにもStanzaにもRTX3070を使用できているため、この設定は後輩に託そうと考えている。

### 2.3 StanzaとspaCyによる文章分割の修正と比較
stanzaを実行するにあたって、RTX3070とPyTorchのバージョンが適合していなかったため、適したバージョンのPyTorchをインストールした。
```
sudo python3 -m pip uninstall torch
pip3 install torch==1.8.2+cu111 torchvision==0.9.2+cu111 torchaudio==0.8.2 -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html
```

[8] [Start Locally](https://pytorch.org/get-started/locally/)

StanzaとspaCyでそれぞれ30件*3か国の記事を文章分割したところ、Stanzaは約8.9秒、spaCyは約62.0秒かかった。
これは、公式ドキュメントによる「大量のテキスト処理のためにはルールベースのspaCyの方が適している」という記述と矛盾する結果である。
分割精度においても以下のようにStanzaの方が優れているため、spaCyではなくStanzaを利用することとした。
Stanzaでも省略のピリオドの判定に失敗している例が見受けられたが、Stanzaと同等のツールを導入するのはコストが高いため、今後の展望に記述することとする。

```
- spacy
    - 8028.278643369675s
    - 30件*3記事
        - 62.03794503211975秒
        - .\..\.
            - インド2件
                - jadhav also said he owes a lot to former captain m.s.#dhoni who backed him throughout his career and helped him play so many one day internationals odis for the country.#
                    - また、ジャダヴは、キャリアを通じて彼を支え、国のために多くの1日国際試合に出場させてくれたM.S.ドーニ元キャプテンに多くの恩義を感じていると語りました。
                    - m.s.#でミス
                - under the worstcase scenario with no interventions against the virus africa could see 3.3 million deaths and 1.2 billion infections the report by the u.n.#economic commission for africa says.
                    - 国連アフリカ経済委員会の報告書によると、ウイルスへの対策を行わなかった場合、アフリカでは330万人の死亡者と12億人の感染者が出る可能性があります。
                    - u.n.#でミス
            - 日本53件、うち上位2件
                - u.n.（国連）, u.s.(アメリカ), feb. (2月) のミスが多い
                - after the quarantine those from niger can go home but foreigners are taken to u.n.#transit centers in niger where they are stuck because air travel is suspended in and out of the country.
                    - 検疫後、ニジェールの人々は家に帰ることができますが、外国人はニジェールにある国連のトランジットセンターに連れて行かれ、飛行機の発着が停止しているため、身動きが取れなくなります。
                    - u.n.#でミス
                - agra  on feb.#25 a day after u.s.#president donald trump and his wife melania posed for pictures outside the taj mahal on an official visit to india sumit kapoor returned to his nearby home from a trip to italy.#
                    - 2月25日、アグラでは、インドを公式訪問したドナルド・トランプ大統領とメラニア夫人がタージ・マハルの外で写真を撮った翌日、スミット・カプールがイタリア旅行から自宅近くに戻ってきました。
                    - feb.#25でミス
            - 韓国5件
                - a.m.はうまくいっている
                - the country on which we put the foremost priority is the u.s.#as there has been a spike in new infections there and president donald trump has also made a request to us himself while the us has not barred the entry of our citizens and struck a currency swap deal with south korea the official said.
                    - u.s.#asでミス
                    - アメリカでは新たな感染者が急増しており、ドナルド・トランプ大統領も自らアメリカに要請していますが、アメリカは国民の入国を禁止しておらず、韓国と通貨スワップ協定を結んでいます。
        - #.\.
            - インド0件
            - 日本4件
                - #u.s.#president donald trump and senior u.s.#officials have accused china of withholding details about how the coronavirus oubreak began in wuhan late last year.
                    - ドナルド・トランプ米大統領と米政府高官は、中国が昨年末に武漢で発生したコロナウイルスの感染経路について詳細を隠していると非難した。
                    - #u.s.#でミス
                - #u.s.#president donald trumps political opponents have accused him of lashing out at china a geopolitical foe but critical u.s.#trade partner in an attempt to deflect criticism at home.
                    - 米国のドナルド・トランプ大統領は、地政学上の敵であると同時に米国の重要な貿易相手国でもある中国を非難し、国内の批判を避けようとしていると、政敵から非難されています。
                    - #u.s.#でミス
            - 韓国0件
        - #..\.
            - インド2件
                - #dr.#gadre said late admissions could be one of the causes for the high deaths at sassoon.#
                    - ガドレ博士は、入院が遅かったことが、サスーンでの高い死亡率の原因の一つではないかと話しています。
                    - #dr.#でミス
                        - dr.が1文に見なされている
                - #dr.#gadre noted that public hospitals like sassoon and king edwards memorial hospital kem were heavily overloaded with patients and were doing enormous work compared to their capacity.#
                    - Gadre博士は、SassoonやKing Edwards Memorial Hospital Kemなどの公立病院は、患者数が非常に多く、その能力に比べて膨大な作業を行っていると指摘しました。
                    - #dr.#でミス
                        - dr.が1文に見なされている
            - 日本4件
                - #australian media reported saturday that the nrl plans a 20round season in a revised schedule with the grand final championship to be played on oct.#25.#
                    - oct.#25でミス
                    - オーストラリアのメディアが土曜日に報じたところによると、NRLはシーズンを20ラウンドに変更し、グランドファイナル・チャンピオンシップは10月25日に行われる予定です。
                - .#dr.#brajendra singh chandel a surveillance medical officer with the world health organization in agra said he pulled out vaccination microplans that had been developed for polio control by the who using them alongside google maps to plot target areas.#
                    - #dr.#でミス
                        - dr.が1文に見なされている
            - 韓国0件
- stanza
    - 30件*3記事
        - 8.87275s
        - .\..\.
            - インド2件
                - #jadhav also said he owes a lot to former captain m.s. dhoni who backed him throughout his career and helped him play so many one day internationals odis for the country.#
                    - また、ジャダヴは、キャリアを通じて彼を支え、国のために多くの1日国際試合に出場させてくれたM.S.ドーニ元キャプテンに多くの恩義を感じていると語りました。
                    - m.s.で成功
                - #under the worstcase scenario with no interventions against the virus africa could see 3.3 million deaths and 1.2 billion infections the report by the u.n. economic commission for africa says.#
                    - 国連アフリカ経済委員会の報告書によると、ウイルスへの対策を行わなかった場合、アフリカでは330万人の死亡者と12億人の感染者が出る可能性があります。
                    - u.n.で成功
            - 日本53件
                - #on the bright side the switch would enhance the international flow of students by staying in line with the school year calendars in the u.s. and europe the report said.#
                    - また、アメリカやヨーロッパの学年暦に合わせて変更することで、国際的な学生の流れを促進することができるとしています。
                    - u.s.で成功
                - #25 a day after u.s. president donald trump and his wife melania posed for pictures outside the taj mahal on an official visit to india sumit kapoor returned to his nearby home from a trip to italy.#
                    - 25 インドを公式訪問したドナルド・トランプ大統領とメラニア夫人がタジ・マハールの外で写真を撮った翌日、スミット・カプーアはイタリア旅行から自宅近くに戻ってきました。
                    - u.s.で成功
            - 韓国5件
                - #pansori show red cliff jeongdong theaterinstead for patrons who had been eagerly awaiting the show jeongdong theater will stream the show live wednesday at 8 p.m. through its youtube channel.#
                    - pansori show red cliff jeongdong theater（パンソリ・ショー レッドクリフ チョンドン・シアター）この公演を心待ちにしていたお客様のために、チョンドン・シアターでは水曜日の午後8時からyoutubeチャンネルでライブ配信を行います。
                    - p.m.で成功
                - #market kurly offers a wide range of groceries and merchandise for delivery by 7 a.m. the next day for orders placed before 11 p.m.according to app retail data service wiseappwiseretail market kurly is estimated to have recorded 60.4 billion won 51.9 million in sales in february marking a 40 percent increase from january.#
                    - p.m.で区切ってほしいが失敗
                    - WiseApp/WiseRetailがwiseappwiseretailになっている
                        - 同じ固有名詞として捉えられるので問題は無さそう
        - #.\.
            - インド0件
            - 日本5件
                - #u.s. president donald trump and senior u.s. officials have accused china of withholding details about how the coronavirus oubreak began in wuhan late last year.#
                    - ドナルド・トランプ米大統領と米政府高官は、中国が昨年末に武漢で発生したコロナウイルスの感染経路について詳細を隠していると非難した。
                    - u.s.で2回成功
                - #u.s. president donald trumps political opponents have accused him of lashing out at china a geopolitical foe but critical u.s. trade partner in an attempt to deflect criticism at home.#
                    - 米国のドナルド・トランプ大統領は、地政学上の敵であると同時に米国の重要な貿易相手国でもある中国を非難し、国内の批判を避けようとしていると、政敵から非難されています。
                    - u.s.で成功
            - 韓国0件
        - #..\.
            - インド3件
                - #dr. gadre said late admissions could be one of the causes for the high deaths at sassoon.#
                    - ガドレ博士は、入院時期が遅かったことが、サスーンでの高い死亡率の原因の一つではないかと述べています。
                    - dr.で成功
                - #dr. gadre noted that public hospitals like sassoon and king edwards memorial hospital kem were heavily overloaded with patients and were doing enormous work compared to their capacity.#
                    - Gadre博士は、SassoonやKing Edwards Memorial Hospital Kemなどの公立病院は、患者数が非常に多く、その能力に比べて膨大な作業を行っていると指摘しました。
                    - Dr.で成功
            - 日本4件
                - #australian media reported saturday that the nrl plans a 20round season in a revised schedule with the grand final championship to be played on oct.#25. the match venues have not been determined although they are all expected to be in new south wales.#
                    - oct.#25.で失敗
                - #dr. brajendra singh chandel a surveillance medical officer with the world health organization in agra said he pulled out vaccination microplans that had been developed for polio control by the who using them alongside google maps to plot target areas.#
                    - アグラの世界保健機関（WHO）の監視医療官であるブラジェンドラ・シン・チャンデル博士は、ポリオ対策のために開発されたワクチン接種のマイクロプランを取り出し、グーグルマップと併用してターゲットエリアを設定したという。
                    - Dr.で成功
            - 韓国0件
```

なお、全記事を分割したところ、Stanzaは約8028.2秒かかり、spaCyは以下のエラーで終了してしまった。
英語モデルのdevブランチを利用することで解決するという情報を得たが[9]、そのための具体的な方法を見つけることができなかった。
90件の処理結果ではspaCyよりStanzaの方が速度、精度ともに優れているため、問題解決は保留してStanzaを利用することとする。

```
  Traceback (most recent call last):
  File "/home/nagi/.local/lib/python3.6/site-packages/stanza/models/constituency/lstm_model.py", line 285, in initial_word_queues
    tag_idx = torch.stack([self.tag_tensors[self.tag_map[word.label]] for word in tagged_words])
  File "/home/nagi/.local/lib/python3.6/site-packages/stanza/models/constituency/lstm_model.py", line 285, in <listcomp>
    tag_idx = torch.stack([self.tag_tensors[self.tag_map[word.label]] for word in tagged_words])
KeyError: 'GW'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "preprocess_03_split_sentences.py", line 115, in <module>
    main()
  File "preprocess_03_split_sentences.py", line 95, in main
    doc = nlp(line)
  File "/home/nagi/.local/lib/python3.6/site-packages/stanza/pipeline/core.py", line 231, in __call__
    doc = self.process(doc)
  File "/home/nagi/.local/lib/python3.6/site-packages/stanza/pipeline/core.py", line 225, in process
    doc = process(doc)
  File "/home/nagi/.local/lib/python3.6/site-packages/stanza/pipeline/constituency_processor.py", line 50, in process
    trees = trainer.parse_tagged_words(self._model.model, words, self._batch_size)
  File "/home/nagi/.local/lib/python3.6/site-packages/stanza/models/constituency/trainer.py", line 545, in parse_tagged_words
    treebank = parse_sentences(sentence_iterator, build_batch_from_tagged_words, batch_size, model)
  File "/home/nagi/.local/lib/python3.6/site-packages/stanza/models/constituency/trainer.py", line 501, in parse_sentences
    tree_batch = build_batch_fn(batch_size, data_iterator, model)
  File "/home/nagi/.local/lib/python3.6/site-packages/stanza/models/constituency/trainer.py", line 485, in build_batch_from_tagged_words
    tree_batch = parse_transitions.initial_state_from_words(tree_batch, model)
  File "/home/nagi/.local/lib/python3.6/site-packages/stanza/models/constituency/parse_transitions.py", line 139, in initial_state_from_words
    return initial_state_from_preterminals(preterminal_lists, model, gold_trees=None)
  File "/home/nagi/.local/lib/python3.6/site-packages/stanza/models/constituency/parse_transitions.py", line 112, in initial_state_from_preterminals
    word_queues = model.initial_word_queues(preterminal_lists)
  File "/home/nagi/.local/lib/python3.6/site-packages/stanza/models/constituency/lstm_model.py", line 289, in initial_word_queues
    raise KeyError("Constituency parser not trained with tag {}".format(str(e))) from e
KeyError: "Constituency parser not trained with tag 'GW'"
```

[9] [KeyError: "Constituency parser not trained with tag 'GW'" #862](https://githubmemory.com/repo/stanfordnlp/stanza/issues/862)

## 3. 次回までに実施予定であること
- EvidenceとClaimの分類
- クラスタリングの実装

## 4. メモ
- 報告会での実行を止め忘れてフリーズ
    - 志田くんに再起動してもらった
- venvのpath
    - [How do you set your pythonpath in an already-created virtualenv?](https://stackoverflow.com/questions/4757178/how-do-you-set-your-pythonpath-in-an-already-created-virtualenv)
        - venvのactivate時にpathを通す
            - bin/activateにexport PYTHONPATH="path名" を追加
        - deactivate時に戻したければ
            - その前にexport OLD_PYTHONPATH="$PYTHONPATH" を書いてストック
            - bin/postdeactivateに export PYTHONPATH="$OLD_PYTHONPATH" を追加
- treeの更新
    - apt install tree
    - tree -d -I "tmp|out|img"
        - -L 3 で深さ指定
    - 改行用のスペースに注意
- Gitリモートに対して認証できず
    - VSCodeでSSH接続
        - [Visual Studio Code で Remote SSH する。](https://qiita.com/nlog2n2/items/1d1358f6913249f3e186)
            - Remote SSH
            - ssh-keygen -t rsa -b 2048 -f ~/.ssh/nagi_lab
        - [Visual Studio CodeでLinux ホストリモート開発](https://qiita.com/whim0321/items/ae72b2dd5fd41beaef04)
            - OpenSSH互換クライアントの確認
                - Get-WindowsCapability -Online | ? Name -like 'OpenSSH.Client*'
                    - なければAdd-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0
            - 鍵生成
                - C:\> ssh-keygen -t rsa -b 4096
                    - 3回Enter
            - 鍵の転送
                - 接続先のLinuxサーバのユーザ、IPの設定
                    - C:\> SET REMOTEHOST=[ユーザ名]@[host名 or IPアドレス]
                - ssh公開鍵のコピー
                    - C:\> scp %USERPROFILE%\.ssh\id_rsa.pub %REMOTEHOST%:~/tmp.pub
                        - powershellでは上手くいかなかった
                    - C:\> ssh %REMOTEHOST% "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat ~/tmp.pub >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys && rm -f ~/tmp.pub"
            - 接続確認
                - ssh -i %USERPROFILE%\.ssh\id_rsa %REMOTEHOST%
            - VScodeでRemote Developmentをインストール
            - 接続
                - VSCodeでF1->Remote SSH->nagi@ip
                - もしくはConnect Current ~
- 3070の増設
    - CPUのソケットを逆に挿して苦戦
    - 起動時、 started gnome display manager の項目で止まる
        - SSH接続したCUIでsudo ubuntu-drivers autoinstall でGUIに入れた
- ubuntuの画面が真っ暗
    - ログインしたままだと良くない
- 映像出力の設定
    - GT710のスロットはすぐ隣で良かったのか
    - xorg.conf
        - [GPUボードが複数ある Ubuntu 20.04でディスプレイ出力に使うGPUを指定したい](https://ja.stackoverflow.com/questions/74811/gpu%E3%83%9C%E3%83%BC%E3%83%89%E3%81%8C%E8%A4%87%E6%95%B0%E3%81%82%E3%82%8B-ubuntu-20-04%E3%81%A7%E3%83%87%E3%82%A3%E3%82%B9%E3%83%97%E3%83%AC%E3%82%A4%E5%87%BA%E5%8A%9B%E3%81%AB%E4%BD%BF%E3%81%86gpu%E3%82%92%E6%8C%87%E5%AE%9A%E3%81%97%E3%81%9F%E3%81%84)
            - GPUのID確認
                - lspci | grep VGA
            - confファイルの作成
                - sudo nvidia-xconfig
            - IDを10進数に変換し、confに追加
            - 再起動
    - 表示の別手段
        - [Ubuntu 18.04 で、NVIDIAのリポジトリを利用してtensorflow-gpu環境を構築するシンプルな方法](https://www.nemotos.net/?p=3176)
        - NVIDIAに絞って表示
            - lspci | grep -i nvidia
        - 型番情報のアップデート
            - sudo update-pciids
                - 3070しか表示されない
                    - 挿すPCIスロットが異なる？
                    - 710を3070と離れた位置に挿すべきだった？
                        - クロックか電力か何か問題があった気がする
                    - 3070はCPUに遠い場所に挿すべきだった？
                        - 710がメインになりそう
                        - 3070が同じ症状になるかも
                    - 映像出力を710に設定するのは理想であり必須ではない
                        - 後輩に任せる？
    - マシンスペック確認
        - [Linuxでコマンドラインからマシンスペックを確認する方法](https://qiita.com/DaisukeMiyamoto/items/98ef077ddf44b5727c29)
        - メモリ
            - cat /proc/meminfo
                - 32GB
        - nvidia-smi
            - driver 470.82.00
            - cuda 11.4
    - aptだと古いNVIDIAドライバーまでしか入らない？
    - 推奨ドライバの確認
        - ubuntu-drivers decices
            - recommendedがインストールされていない
            - 再びubuntu-drivers autoinstall
                - 変更なし
    - NVIDIAのリポジトリからアプデ
        - [UbuntuにNVIDIA driverをインストール/再インストールする方法](https://qiita.com/yto1292/items/463e054943f3076f36cc)
            - sudo add-apt-repository ppa:graphics-drivers/ppa
    - ハードが認識されないのでスロット変えるほか無さそう
        - 映像出力+学習で遅かったら考える
        - CUI+学習にする手もある
- ubuntuのアプデ
    - 困ったらやる感じで
    - nvidia関連のドライバがブレそう
- 3000番台でのTF設定
    - docker image
        - オーバーヘッドがある？
        - OSに依存しない
            - updateで環境が壊れない
        - NVIDIAで安心
        - driver455以上、cuda11.1以上？
            - [Deep Learning 環境の構築 RTX 3000シリーズ 2021/02 更新](https://qiita.com/k_ikasumipowder/items/e711186c329b36f53833)
            - 普通に入った
        - nvidia-smiで表示されるのは推奨ドライバにすぎない？
            - https://blog.mktia.com/get-cuda-and-cudnn-version/
        - 志田くんの資料
            - sudo apt-get -y install cudaで依存関係エラー
                - 一度依存関係をクリーンした
                - recommendedが470->495になった
            - tensorflow-gpuを入れているみたいだが、最新はtensorflow
                - https://www.tensorflow.org/install/pip?hl=ja
                - 古いのはtensorflow==
            - tensorflowのインストールでError13
                - pipのアプデも同様のエラー
                    - --userを付けないとだめらしい
                    - pip 9->21
            - tensorflowのインストールでpathのエラー
                - Will not install to the user site because it will lack sys.path precedence to setuptools in /home/nagi/Documents/git/data-engineering-lab/experiment/venv/lib/python3.6/site-packages
                - ~~venv用にpathを通す必要あり？~~
                - venv作成時に--system-site-packagesを付けていなかった？
                    - 依存関係のエラーが出たが問題はなさそう。無視。
                        - ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.launchpadlib 1.10.6 requires testresources, which is not installed.flake8 4.0.1 requires importlib-metadata<4.3; python_version < "3.8", but you have importlib-metadata 4.8.2 which is incompatible.
            - tensorを返すデバッグ
                - python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
                    - （中略）
                    - tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
                    - tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
                        - このTensorFlowバイナリは、oneAPI Deep Neural Network Library（oneDNN）で最適化されており、パフォーマンスが重視される操作では以下のCPU命令を使用します。 AVX2 FMA その他の処理でこれらの命令を有効にするには、適切なコンパイラフラグでTensorFlowを再構築します。
                    - （中略）
                    - tensorflow/core/common_runtime/gpu/gpu_device.cc:1510] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 6033 MB memory:  -> device: 0, name: NVIDIA GeForce RTX 3070, pci bus id: 0000:01:00.0, compute capability: 8.6 tf.Tensor(-1670.4432, shape=(), dtype=float32)
                        - Tensor返ってそう
                        - 3070が使えていそう
- git cloneし直したら記事のデータ消してしまった
    - 再度作成
    - bashのエラー修正
        - {1..3}->{0..2}
        - $1 -> $i
- venvのactivateを編集
    - cythonは--userでないとパーミッションエラー
        - tf同様--system-site-packagesを付けてvenvを構築するべきだった？
            - グローバルのsite-packagesにインストール済のモジュールを引き継ぐ
                - https://hikm.hatenablog.com/entry/2015/01/22/000448
    - spacyは
    - pip freezeで確認
    - ModuleNotFoundError: No module named 'Cython'
        - https://heppoco-cto.com/pip-install%E3%81%A7scikit-learn%E3%81%AEbuild%E3%81%A7modulenotfounderror-no-module-named-cython%E3%81%AE%E3%82%A8%E3%83%A9%E3%83%BC%E3%81%8C%E5%87%BA%E3%82%8B/483/
            - pip install --upgrade cython
            - 変化なし
        - venvを再構築したら直った
- stanzaの実行
    - pytorchのcuda capabilityでエラー
        - 今のPytorchはsm_37-70に対応
        - 3070はsm_86
        - python3 -c 'import torch; print(torch.__version__)'
            - 1.10.0+cu102
        - pytorchのアプデ
            - https://pytorch.org/get-started/locally/
            - pip3 install torch==1.8.2+cu111 torchvision==0.9.2+cu111 torchaudio==0.8.2 -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html
                - 効果なし
                - 旧torchがuninstallできたか怪しい
                    - 1.10.0+cu102のままだった
            - アンインストール
                - sudo python3 -m pip uninstall torch
                    - sudo -H でないと消しきれないと言われた
                        - 付けたら見つからないと言われた
            - バージョン確認
                - 1.8.2+cu111
                - なんか消えてないけどヨシ
    - タイムと 精度
        - spacy
            - 8028.278643369675s
            - 30件*3記事
                - 62.03794503211975秒
                - .\..\.
                    - インド2件
                        - jadhav also said he owes a lot to former captain m.s.#dhoni who backed him throughout his career and helped him play so many one day internationals odis for the country.#
                            - また、ジャダヴは、キャリアを通じて彼を支え、国のために多くの1日国際試合に出場させてくれたM.S.ドーニ元キャプテンに多くの恩義を感じていると語りました。
                            - m.s.#でミス
                        - under the worstcase scenario with no interventions against the virus africa could see 3.3 million deaths and 1.2 billion infections the report by the u.n.#economic commission for africa says.
                            - 国連アフリカ経済委員会の報告書によると、ウイルスへの対策を行わなかった場合、アフリカでは330万人の死亡者と12億人の感染者が出る可能性があります。
                            - u.n.#でミス
                    - 日本53件、うち上位2件
                        - u.n.（国連）, u.s.(アメリカ), feb. (2月) のミスが多い
                        - after the quarantine those from niger can go home but foreigners are taken to u.n.#transit centers in niger where they are stuck because air travel is suspended in and out of the country.
                            - 検疫後、ニジェールの人々は家に帰ることができますが、外国人はニジェールにある国連のトランジットセンターに連れて行かれ、飛行機の発着が停止しているため、身動きが取れなくなります。
                            - u.n.#でミス
                        - agra  on feb.#25 a day after u.s.#president donald trump and his wife melania posed for pictures outside the taj mahal on an official visit to india sumit kapoor returned to his nearby home from a trip to italy.#
                            - 2月25日、アグラでは、インドを公式訪問したドナルド・トランプ大統領とメラニア夫人がタージ・マハルの外で写真を撮った翌日、スミット・カプールがイタリア旅行から自宅近くに戻ってきました。
                            - feb.#25でミス
                    - 韓国5件
                        - a.m.はうまくいっている
                        - the country on which we put the foremost priority is the u.s.#as there has been a spike in new infections there and president donald trump has also made a request to us himself while the us has not barred the entry of our citizens and struck a currency swap deal with south korea the official said.
                            - u.s.#asでミス
                            - アメリカでは新たな感染者が急増しており、ドナルド・トランプ大統領も自らアメリカに要請していますが、アメリカは国民の入国を禁止しておらず、韓国と通貨スワップ協定を結んでいます。
                - #.\.
                    - インド0件
                    - 日本4件
                        - #u.s.#president donald trump and senior u.s.#officials have accused china of withholding details about how the coronavirus oubreak began in wuhan late last year.
                            - ドナルド・トランプ米大統領と米政府高官は、中国が昨年末に武漢で発生したコロナウイルスの感染経路について詳細を隠していると非難した。
                            - #u.s.#でミス
                        - #u.s.#president donald trumps political opponents have accused him of lashing out at china a geopolitical foe but critical u.s.#trade partner in an attempt to deflect criticism at home.
                            - 米国のドナルド・トランプ大統領は、地政学上の敵であると同時に米国の重要な貿易相手国でもある中国を非難し、国内の批判を避けようとしていると、政敵から非難されています。
                            - #u.s.#でミス
                    - 韓国0件
                - #..\.
                    - インド2件
                        - #dr.#gadre said late admissions could be one of the causes for the high deaths at sassoon.#
                            - ガドレ博士は、入院が遅かったことが、サスーンでの高い死亡率の原因の一つではないかと話しています。
                            - #dr.#でミス
                                - dr.が1文に見なされている
                        - #dr.#gadre noted that public hospitals like sassoon and king edwards memorial hospital kem were heavily overloaded with patients and were doing enormous work compared to their capacity.#
                            - Gadre博士は、SassoonやKing Edwards Memorial Hospital Kemなどの公立病院は、患者数が非常に多く、その能力に比べて膨大な作業を行っていると指摘しました。
                            - #dr.#でミス
                                - dr.が1文に見なされている
                    - 日本4件
                        - #australian media reported saturday that the nrl plans a 20round season in a revised schedule with the grand final championship to be played on oct.#25.#
                            - oct.#25でミス
                            - オーストラリアのメディアが土曜日に報じたところによると、NRLはシーズンを20ラウンドに変更し、グランドファイナル・チャンピオンシップは10月25日に行われる予定です。
                        - .#dr.#brajendra singh chandel a surveillance medical officer with the world health organization in agra said he pulled out vaccination microplans that had been developed for polio control by the who using them alongside google maps to plot target areas.#
                            - #dr.#でミス
                                - dr.が1文に見なされている
                    - 韓国0件
        - stanza
            - 30件*3記事
                - 8.87275s
                - .\..\.
                    - インド2件
                        - #jadhav also said he owes a lot to former captain m.s. dhoni who backed him throughout his career and helped him play so many one day internationals odis for the country.#
                            - また、ジャダヴは、キャリアを通じて彼を支え、国のために多くの1日国際試合に出場させてくれたM.S.ドーニ元キャプテンに多くの恩義を感じていると語りました。
                            - m.s.で成功
                        - #under the worstcase scenario with no interventions against the virus africa could see 3.3 million deaths and 1.2 billion infections the report by the u.n. economic commission for africa says.#
                            - 国連アフリカ経済委員会の報告書によると、ウイルスへの対策を行わなかった場合、アフリカでは330万人の死亡者と12億人の感染者が出る可能性があります。
                            - u.n.で成功
                    - 日本53件
                        - #on the bright side the switch would enhance the international flow of students by staying in line with the school year calendars in the u.s. and europe the report said.#
                            - また、アメリカやヨーロッパの学年暦に合わせて変更することで、国際的な学生の流れを促進することができるとしています。
                            - u.s.で成功
                        - #25 a day after u.s. president donald trump and his wife melania posed for pictures outside the taj mahal on an official visit to india sumit kapoor returned to his nearby home from a trip to italy.#
                            - 25 インドを公式訪問したドナルド・トランプ大統領とメラニア夫人がタジ・マハールの外で写真を撮った翌日、スミット・カプーアはイタリア旅行から自宅近くに戻ってきました。
                            - u.s.で成功
                    - 韓国5件
                        - #pansori show red cliff jeongdong theaterinstead for patrons who had been eagerly awaiting the show jeongdong theater will stream the show live wednesday at 8 p.m. through its youtube channel.#
                            - pansori show red cliff jeongdong theater（パンソリ・ショー レッドクリフ チョンドン・シアター）この公演を心待ちにしていたお客様のために、チョンドン・シアターでは水曜日の午後8時からyoutubeチャンネルでライブ配信を行います。
                            - p.m.で成功
                        - #market kurly offers a wide range of groceries and merchandise for delivery by 7 a.m. the next day for orders placed before 11 p.m.according to app retail data service wiseappwiseretail market kurly is estimated to have recorded 60.4 billion won 51.9 million in sales in february marking a 40 percent increase from january.#
                            - p.m.で区切ってほしいが失敗
                            - WiseApp/WiseRetailがwiseappwiseretailになっている
                                - 同じ固有名詞として捉えられるので問題は無さそう
                - #.\.
                    - インド0件
                    - 日本5件
                        - #u.s. president donald trump and senior u.s. officials have accused china of withholding details about how the coronavirus oubreak began in wuhan late last year.#
                            - ドナルド・トランプ米大統領と米政府高官は、中国が昨年末に武漢で発生したコロナウイルスの感染経路について詳細を隠していると非難した。
                            - u.s.で2回成功
                        - #u.s. president donald trumps political opponents have accused him of lashing out at china a geopolitical foe but critical u.s. trade partner in an attempt to deflect criticism at home.#
                            - 米国のドナルド・トランプ大統領は、地政学上の敵であると同時に米国の重要な貿易相手国でもある中国を非難し、国内の批判を避けようとしていると、政敵から非難されています。
                            - u.s.で成功
                    - 韓国0件
                - #..\.
                    - インド3件
                        - #dr. gadre said late admissions could be one of the causes for the high deaths at sassoon.#
                            - ガドレ博士は、入院時期が遅かったことが、サスーンでの高い死亡率の原因の一つではないかと述べています。
                            - dr.で成功
                        - #dr. gadre noted that public hospitals like sassoon and king edwards memorial hospital kem were heavily overloaded with patients and were doing enormous work compared to their capacity.#
                            - Gadre博士は、SassoonやKing Edwards Memorial Hospital Kemなどの公立病院は、患者数が非常に多く、その能力に比べて膨大な作業を行っていると指摘しました。
                            - Dr.で成功
                    - 日本4件
                        - #australian media reported saturday that the nrl plans a 20round season in a revised schedule with the grand final championship to be played on oct.#25. the match venues have not been determined although they are all expected to be in new south wales.#
                            - oct.#25.で失敗
                        - #dr. brajendra singh chandel a surveillance medical officer with the world health organization in agra said he pulled out vaccination microplans that had been developed for polio control by the who using them alongside google maps to plot target areas.#
                            - アグラの世界保健機関（WHO）の監視医療官であるブラジェンドラ・シン・チャンデル博士は、ポリオ対策のために開発されたワクチン接種のマイクロプランを取り出し、グーグルマップと併用してターゲットエリアを設定したという。
                            - Dr.で成功
                    - 韓国0件
        - DeepLは省略のピリオドをうまく判別してくれている
    - stanzaとspacyでファイル名変えて保存
        - foreachはコピーを作成するため編集できないことに注意
            - rangeかenumurateか内包表記
    - spacyを夜回したらエラー
        - 2回目も割と早め
```
  Traceback (most recent call last):
  File "/home/nagi/.local/lib/python3.6/site-packages/stanza/models/constituency/lstm_model.py", line 285, in initial_word_queues
    tag_idx = torch.stack([self.tag_tensors[self.tag_map[word.label]] for word in tagged_words])
  File "/home/nagi/.local/lib/python3.6/site-packages/stanza/models/constituency/lstm_model.py", line 285, in <listcomp>
    tag_idx = torch.stack([self.tag_tensors[self.tag_map[word.label]] for word in tagged_words])
KeyError: 'GW'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "preprocess_03_split_sentences.py", line 115, in <module>
    main()
  File "preprocess_03_split_sentences.py", line 95, in main
    doc = nlp(line)
  File "/home/nagi/.local/lib/python3.6/site-packages/stanza/pipeline/core.py", line 231, in __call__
    doc = self.process(doc)
  File "/home/nagi/.local/lib/python3.6/site-packages/stanza/pipeline/core.py", line 225, in process
    doc = process(doc)
  File "/home/nagi/.local/lib/python3.6/site-packages/stanza/pipeline/constituency_processor.py", line 50, in process
    trees = trainer.parse_tagged_words(self._model.model, words, self._batch_size)
  File "/home/nagi/.local/lib/python3.6/site-packages/stanza/models/constituency/trainer.py", line 545, in parse_tagged_words
    treebank = parse_sentences(sentence_iterator, build_batch_from_tagged_words, batch_size, model)
  File "/home/nagi/.local/lib/python3.6/site-packages/stanza/models/constituency/trainer.py", line 501, in parse_sentences
    tree_batch = build_batch_fn(batch_size, data_iterator, model)
  File "/home/nagi/.local/lib/python3.6/site-packages/stanza/models/constituency/trainer.py", line 485, in build_batch_from_tagged_words
    tree_batch = parse_transitions.initial_state_from_words(tree_batch, model)
  File "/home/nagi/.local/lib/python3.6/site-packages/stanza/models/constituency/parse_transitions.py", line 139, in initial_state_from_words
    return initial_state_from_preterminals(preterminal_lists, model, gold_trees=None)
  File "/home/nagi/.local/lib/python3.6/site-packages/stanza/models/constituency/parse_transitions.py", line 112, in initial_state_from_preterminals
    word_queues = model.initial_word_queues(preterminal_lists)
  File "/home/nagi/.local/lib/python3.6/site-packages/stanza/models/constituency/lstm_model.py", line 289, in initial_word_queues
    raise KeyError("Constituency parser not trained with tag {}".format(str(e))) from e
KeyError: "Constituency parser not trained with tag 'GW'"
```
- spacyのエラー修正
    - KeyError: "Constituency parser not trained with tag 'GW'"
        - https://githubmemory.com/repo/stanfordnlp/stanza/issues/862
            - ENモデルのdevブランチを取ってくる？
            - 小さい文章でもなるらしい
    - raise KeyError("Constituency parser not trained with tag {}".format(str(e))) from e
    - 
