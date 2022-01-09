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

# 週次報告書 2021年12月01日
AL18036 片岡 凪

## 1. 今回の報告会までに実施する予定だったこと
- EvidenceとClaimの分類
- ~~クラスタリングの実装~~

## 2. 実施内容

### 目次
- 2.1 全てのプログラムを実装できるレベルで設計
- 2.2 予備実験の主張-出来事分類の移植の完了

### 2.1 全てのプログラムを実装できるレベルで設計
無駄な実装を減らし、タスクを明確化してやる気を出すため、評価以外の**全てのプログラムを実装レベルで設計した。**

```
- TODO
    - 全体的に
        - printデバッグを増やす
            - オリジナルのprint_debug()を作成
                - import
            - xqq君のjavaコードを参照
        - オプションでアルゴリズムを可変に
        - 後で何かやりたくなったときにできるように余分に処理しとく
        - こまめに記事をバックアップ
    - 主張と出来事の分類
        - process_00_train_classifier_as_claim_or_evidence.py
        - process_01_exe_classifier_as_claim_or_evidence.py
        - india-articles_process-01_classified-claim-or-evidence.txt
        - 日本記事を3か国の記事に変更
            - for with openではなく、複数のファイル名を指定して実行
                - 別にファイル名のtxtファイルを作成
                - 長くて指定が面倒なのでやっぱりfor with open
                    - no time
        - #を元にリストに格納
        - 分類
            - 時間かかるからpyにした方がいいかも
        - #e;feature-x;feature-y;sent-1#c;feature-x;feature-y;sent-2...\n のtxt
            - DeepL翻訳で10記事ほどチェック
            - 文頭、文末はシャープがないことに注意
        - ニュートラルも含めることを考えつつ
        - シャッフルを消す
            - 前処理前の記事との紐づけのため
            - 本当は必要
    - 出来事の文章の特徴量ベクトルを作成
        - process_02_articles_features_calculator.py
        - india-articles_process-02_calced-articles-features.txt
        - 出来事の文のみを結合
            - 一応主張、全文も作っておく
        - SBERTに入れる
        - 文頭にarticle-n;[e-feature-array];[c-feature-array];[all-feature-array]#を追加
    - 主張の文の特徴量ベクトルを作成
        - process_03_sentences_features_calculator.py
        - india-articles_process-03_calced-sentences-features.txt
        - #e:sent-1#c:sent-2...\n
        - S-BERTにsent-nを入れて特徴量を算出
        - article-n;[e-feature-array];[c-feature-array];[all-feature-array]#article-n;sentence-n;e;feature-x;feature-y;[feature-array];sent-1#article-n;sentence-n;c;feature-x;feature-y;[feature-array];sent-2...\n とする
            - 各文に特徴量を追加
            - 各文に番号を追加
            - #eのfeatureは不要だが、もしかしたら使うかも
        - txt保存
    - 3カ国の記事を結合して保存
        - process_04_nations_articles_concatenator.py
        - process-04_concatenated-nations-articles.txt
        - 国情報を付与
            - nation-name;article-n;[e-feature-array];[c-feature-array];[all-feature-array]#nation-name;article-n;sentence-n;e;feature-x;feature-y;[feature-array];sent-1#nation-name;article-n;sentence-n;c;feature-x;feature-y;[feature-array];sent-2...\n
    - [e-feature-array]を基に記事（行）をクラスタリング
        - process_05_articles_cluster_generator.py
        - クラスタごとに名前を付けて保存
            - process-05_generated-articles-cluster_n.txt
        - アルゴリズムはオプションで変更
            - ファイル名の末尾にアルゴリズム名
        - クラスタの粒度
    - ある記事のある文章から、似た文章とその文章が書かれた記事が参照できるか
        - 出来事の記事クラスタからnation-name;article-n;sentence-nで記事を特定
        - 主張の文のクラスタリング
        - 主張の文クラスタからnation-name;article-n;sentence-nで文とそのクラスタを特定
        - クラスタごとの主張の差異を分析
    - 出来事の記事クラスタからnation-name;article-n;sentence-nで記事を特定
        - process-06_find-articles-cluster-of-selected-sentence-info.sh
    - 指定した記事クラスタファイルの文を、cの[feature-array]でクラスタリング
        - process-07_sentences_cluster_generator.py
        - クラスタごとに名前を付けて保存
            - process-07_generated-sentences-cluster_n.txt
        - 出来事の記事クラスタからnation-name;article-n;sentence-nで記事を特定
            - デバッグのため、後で実装
        - その記事クラスタファイルを開く
        - #で分割し、cの区分のみを1つのリストに格納
        - リストの要素を[feature-array]を基にクラスタリング
        - クラスタリング手法を変えやすいように
            - オプションで変更
            - 変更できるライブラリ
    - 主張の文クラスタからnation-name;article-n;sentence-nで文とそのクラスタを特定
        - process-08_find-sentences-cluster-of-selected-sentence-info.sh
    - 評価
        - 論文を読んで決める
    - まとめ
        - sent-1#sent-2#...\n
        - e;feature-x;feature-y;sent-1#c;feature-x;feature-y;sent-2...\n 
        - article-n;[e-feature-array];[c-feature-array];[all-feature-array]#e;feature-x;feature-y;sent-1#c;feature-x;feature-y;sent-2...\n
        - article-n;[e-feature-array];[c-feature-array];[all-feature-array]#article-n;sentence-n;e;feature-x;feature-y;[feature-array];sent-1#article-n;sentence-n;c;feature-x;feature-y;[feature-array];sent-2...\n
        - nation-name;article-n;[e-feature-array];[c-feature-array];[all-feature-array]#nation-name;article-n;sentence-n;e;feature-x;feature-y;[feature-array];sent-1#nation-name;article-n;sentence-n;c;feature-x;feature-y;[feature-array];sent-2...\n
        - process-05_generated-articles-cluster_n.txt
        - process-06_find-articles-cluster-of-selected-sentence-info.sh
        - process-07_sentences_cluster_generator.py
        - process-08_find-sentences-cluster-of-selected-sentence-info.sh
```

先週までの前処理で
```
sentence-1#sentence-2#...\n
sentence-1#sentence-2#...\n
...
```
といったデータになっているが、**最終的には**
```
nation-name;article-n;[e-feature-array];[c-feature-array];[all-feature-array]#nation-name;article-n;sentence-n;e;feature-x;feature-y;[feature-array];sent-1#nation-name;article-n;sentence-n;c;feature-x;feature-y;[feature-array];sent-2...\n
〃
...
```
**といったデータを目指す。**
ここで、eはevidence、cはclaim、allは記事全文を表す。

このデータを基に、
1. **出来事の記事のクラスタの複数のtxtファイルを作成し**
2. **閲覧している文章から該当するクラスタを特定し**
3. **該当するクラスタを主張の文でクラスタリングし**
4. **再び閲覧している文章から該当するクラスタを特定する**

大小含めて9つのモジュールを追加で実装する必要があり、2つのモジュールの実装を終えた。
時間がないため、次週までに7つのモジュールを完成させたい。


### 2.2 予備実験の主張-出来事分類の移植の完了
予備実験で行った主張の文と出来事の文の分類は、時間とストレージの関係でColaboratoryの制限を受けていた。
従って、コードを**pyファイルに書き換え**、研究室のPCの環境構築を行ってローカルで実行した。
書き換えにあたり、複数の記事の、新しい前処理のフォーマットに対応させた。
また、予測時間の計測機能を追加した。

IBM Debater Datasets の学習では、**10エポックでprecision~0.999955, accuracy~99.642**となった。
また、**分類には1記事あたり約4秒**の処理時間を要し、少し実用性に欠けている可能性がある。
**ニュースサイトで1日何件の記事が更新されているのかを調査**し、プログラム全体の処理時間と照合して**実用性を考察**する必要がある。


以下に3か国の分類結果を1記事ずつ示す。
```
# インド
e;5.9609375;-6.01171875;the maharashtra government on friday ordered landlords to delay rent collection by at least three months and to not evict tenants from their properties during that period as the nation battles the coronavirus pandemic.#
e;2.373046875;-2.5;there is also a countrywide lockdown in place till may 3 to halt the spread of deadly coronavirus infection.#
e;5.95703125;-6.0078125;maharashtra delhi and tamil nadu continue to struggle with the rising number of coronavirus cases.#
e;5.94140625;-6.0;these states together with rajasthan and madhya pradesh account for more than 60 of total number of cases in the country.#
e;5.96484375;-6.00390625;prime minister narendra modi in his appeal to the nation urged citizens to be sensitive to people who work with them in their businesses.#
e;2.203125;-2.21484375;he also advised them not to sack people working for them.#
e;5.96484375;-6.01171875;maharashtra deputy chief minister ajit pawar has asked all guardian ministers to ensure smooth distribution of food grains to the poor during the covid19 lockdown so that the government is not defamed unnecessarily.#
e;5.9609375;-6.01171875;earlier today the reserve bank of india rbi announced a series of measures to infuse liquidity in the system and provide relief to borrowers amid the crisis.#
e;5.96875;-6.0078125;to begin with rbi has cut the reverse repo rate by 25 basis points  from 4 to 3.75  encouraging banks to deploy surplus funds and lend more a move that will in turn result in cash in the hands of the borrower.#
e;5.96484375;-6.01171875;according to a bloomberg report indias economy may be heading for its first fullyear contraction in more than four decades amid extended lockdown to contain the coronavirus outbreak.

# 日本
e;5.75390625;-5.83984375;sydney  theyre being dubbed the new zealand nomads and with good reason.#
e;5.9609375;-6.0078125;the new zealand warriors of the national rugby league were scheduled to arrive at a small regional airport in new south wales state on sunday after being given permission to enter australia despite a general ban on incoming travelers due to the coronavirus pandemic.#
e;5.9453125;-6.0;during a 14day isolation period during which theyll be able to train at tamworth in the northwestern part of the state theyll likely move down to the central coast north of sydney and play most of their matches in that area once the planned resumption of the season on may 28.#
e;5.94140625;-5.9921875;theyll be without their families for now and will likely not be able to return to new zealand until the nrl season ends.#
e;5.84375;-5.9140625;thats nearly six months from now in october.#
e;5.95703125;-6.00390625;warriors chief executive cameron george hopes families can follow in coming months if current restrictions are relaxed.#
e;5.9609375;-6.01171875;he said an inhouse wellbeing officer will remain with the team during the season while the club will ensure their families have support back in new zealand.#
c;-5.69140625;5.76171875;the club also has the option to apply for a replacement if any player needs to return home prematurely.#
e;5.96484375;-6.0078125;the squad were taking across is the intended squad that we play with for the duration of the season george told australian associated press.#
e;5.88671875;-5.8984375;but if things change for personal reasons for individuals on a casebycase basis we can make application to the nrl particularly on compassionate grounds.#
e;5.91015625;-5.9765625;two nrl rounds were played before the season was suspended on march 23 due to the pandemic.#
e;5.96484375;-6.01171875;australian media reported saturday that the nrl plans a 20round season in a revised schedule with the grand final championship to be played on oct.#
e;5.89453125;-5.96484375;25. the match venues have not been determined although they are all expected to be in new south wales.#
e;5.96484375;-6.01171875;on friday the queensland government said borders would be open for the states three nrl teams to play in new south wales.#
c;-5.70703125;5.75390625;currently there are restrictions on travel between the two states.#
e;5.953125;-6.0078125;it means north queensland brisbane and the gold coast will not need to enter isolation camps in sydney and can remain at home with their families before the season resumes.#
e;5.9609375;-6.01171875;australian states have been easing restriction due to the pandemic with the national covid19 death toll a relatively low 95 midway through sunday and with new cases declining.

# 韓国
e;5.96484375;-6.01171875;bank of korea yonhapincreasingly pressed to play a more active role in the coronavirushit financial market south koreas central bank is considering exceptional measures to provide liquidity such as purchasing corporate bonds and corporate bills.#
e;5.93359375;-5.99609375;the bank of korea is slated to hold its decisionmaking monetary policy board meeting thursday to review the necessity of base rate adjustments and other key monetary actions officials said.#
e;5.96484375;-6.01171875;despite the prolonged economic fallout from the covid19 pandemic and the continued need for easing actions market experts generally suggested that the central bank would freeze the rate this time maintaining a waitandsee approach.#
e;5.96484375;-6.01171875;we expect that the bok will freeze the rate this time so that it may observe the impact of its big rate cut and repo operations which should practically be seen as a quantitative easing action daishin securities analyst gong dongrak said.#
e;5.96484375;-6.00390625;last month the board summoned an emergency session and slashed the nations base rate by 50 basis points to an unprecedented 0.75 percent.#
e;5.96875;-6.0078125;in a followup easing gesture last week the bok funneled some 5.25 trillion won 4.2 billion of liquidity to the financial market through repurchase agreements  or repo operations  essentially providing financial institutions with shortterm loans.#
e;5.96875;-6.00390625;uncertainties remain but the liquidity crunch is showing some signs of alleviation said kim sanghoon of kb securities.#
e;3.775390625;-3.861328125;the bok may prefer to hold off its major decisions at least until the economic indexes for the first quarter shape out.#
e;5.85546875;-5.9296875;some however questioned the effectiveness of the boks policy road map which is relatively passive compared with that of the us federal reserve.#
e;5.95703125;-6.0;last month the us central bank unveiled a primary market corporate credit facility and a secondary market corporate credit facility that would purchase eligible corporate bonds directly from issuers or in the secondary market.#
e;5.9609375;-6.01171875;it also was granted the power to lend an additional 4 trillion to businesses as the us congress approved of an emergency fiscal funding bill to deal with covid19.#
e;5.9609375;-6.01171875;should market situations aggravate the bok could consider providing funds to a special purpose vehicle as an indirect way to purchase corporate bonds from financial companies said jang min a senior researcher at the korea institute of financee;5.74609375;-5.82421875;by bae hyunjung

```

<!-- ```
# インド
the maharashtra government on friday ordered landlords to delay rent collection by at least three months and to not evict tenants from their properties during that period as the nation battles the coronavirus pandemic.
there is also a countrywide lockdown in place till may 3 to halt the spread of deadly coronavirus infection.
maharashtra delhi and tamil nadu continue to struggle with the rising number of coronavirus cases.
these states together with rajasthan and madhya pradesh account for more than 60 of total number of cases in the country.
prime minister narendra modi in his appeal to the nation urged citizens to be sensitive to people who work with them in their businesses.
he also advised them not to sack people working for them.
maharashtra deputy chief minister ajit pawar has asked all guardian ministers to ensure smooth distribution of food grains to the poor during the covid19 lockdown so that the government is not defamed unnecessarily.
earlier today the reserve bank of india rbi announced a series of measures to infuse liquidity in the system and provide relief to borrowers amid the crisis.
to begin with rbi has cut the reverse repo rate by 25 basis points  from 4 to 3.75  encouraging banks to deploy surplus funds and lend more a move that will in turn result in cash in the hands of the borrower.
according to a bloomberg report indias economy may be heading for its first fullyear contraction in more than four decades amid extended lockdown to contain the coronavirus outbreak.

# 日本
sydney  theyre being dubbed the new zealand nomads and with good reason.
the new zealand warriors of the national rugby league were scheduled to arrive at a small regional airport in new south wales state on sunday after being given permission to enter australia despite a general ban on incoming travelers due to the coronavirus pandemic.
during a 14day isolation period during which theyll be able to train at tamworth in the northwestern part of the state theyll likely move down to the central coast north of sydney and play most of their matches in that area once the planned resumption of the season on may 28.
theyll be without their families for now and will likely not be able to return to new zealand until the nrl season ends.
thats nearly six months from now in october.
warriors chief executive cameron george hopes families can follow in coming months if current restrictions are relaxed.
he said an inhouse wellbeing officer will remain with the team during the season while the club will ensure their families have support back in new zealand.
the club also has the option to apply for a replacement if any player needs to return home prematurely.
the squad were taking across is the intended squad that we play with for the duration of the season george told australian associated press.
but if things change for personal reasons for individuals on a casebycase basis we can make application to the nrl particularly on compassionate grounds.
two nrl rounds were played before the season was suspended on march 23 due to the pandemic.
australian media reported saturday that the nrl plans a 20round season in a revised schedule with the grand final championship to be played on oct.
25. the match venues have not been determined although they are all expected to be in new south wales.
on friday the queensland government said borders would be open for the states three nrl teams to play in new south wales.
currently there are restrictions on travel between the two states.
it means north queensland brisbane and the gold coast will not need to enter isolation camps in sydney and can remain at home with their families before the season resumes.
australian states have been easing restriction due to the pandemic with the national covid19 death toll a relatively low 95 midway through sunday and with new cases declining.

# 韓国
bank of korea yonhapincreasingly pressed to play a more active role in the coronavirushit financial market south koreas central bank is considering exceptional measures to provide liquidity such as purchasing corporate bonds and corporate bills.
the bank of korea is slated to hold its decisionmaking monetary policy board meeting thursday to review the necessity of base rate adjustments and other key monetary actions officials said.
despite the prolonged economic fallout from the covid19 pandemic and the continued need for easing actions market experts generally suggested that the central bank would freeze the rate this time maintaining a waitandsee approach.
we expect that the bok will freeze the rate this time so that it may observe the impact of its big rate cut and repo operations which should practically be seen as a quantitative easing action daishin securities analyst gong dongrak said.
last month the board summoned an emergency session and slashed the nations base rate by 50 basis points to an unprecedented 0.75 percent.
in a followup easing gesture last week the bok funneled some 5.25 trillion won 4.2 billion of liquidity to the financial market through repurchase agreements  or repo operations  essentially providing financial institutions with shortterm loans.
uncertainties remain but the liquidity crunch is showing some signs of alleviation said kim sanghoon of kb securities.
the bok may prefer to hold off its major decisions at least until the economic indexes for the first quarter shape out.
some however questioned the effectiveness of the boks policy road map which is relatively passive compared with that of the us federal reserve.
last month the us central bank unveiled a primary market corporate credit facility and a secondary market corporate credit facility that would purchase eligible corporate bonds directly from issuers or in the secondary market.
it also was granted the power to lend an additional 4 trillion to businesses as the us congress approved of an emergency fiscal funding bill to deal with covid19.
should market situations aggravate the bok could consider providing funds to a special purpose vehicle as an indirect way to purchase corporate bonds from financial companies said jang min a senior researcher at the korea institute of financee;by bae hyunjung

``` -->


DeepLを用いて日本語訳すると以下のようになる。
```
# インド　10文
出来事　：マハラシュトラ州政府は金曜日、家主に対し、家賃の徴収を少なくとも3カ月遅らせ、その間は借主を立ち退かせないよう指示しました。
出来事　：また、致命的なコロナウイルスの感染拡大を防ぐために、5月3日まで国全体でロックダウンが実施されています。
出来事　：マハラシュトラ州、デリー州、タミルナドゥ州では、コロナウイルス感染者の増加に苦慮しています。
出来事　：これらの州は、ラジャスタン州、マディヤ・プラデーシュ州とともに、国内の感染者数の60％以上を占めています。
出来事　：ナレンドラ・モディ首相は、国民への呼びかけの中で、ビジネスで共に働く人々に配慮するよう求めました。
出来事　：また、自分のために働いている人を解雇しないようにとのアドバイスもありました。
出来事　：マハラシュトラ州の副首相であるAjit Pawar氏は、政府が不必要に名誉を傷つけられることのないよう、Covid19によるロックダウンの間、貧困層への円滑な食糧配給を確保するよう、すべての保護担当大臣に要請しました。
出来事　：インド準備銀行（RBI）は本日未明、システムに流動性を注入し、危機の中で借り手を救済するための一連の措置を発表した。
出来事　：まず、RBIはリバースレポレートを4から3.75に25ベーシスポイント引き下げ、銀行が余剰資金を活用してより多くの融資を行うことを奨励し、その結果、借り手の手元に現金が届くようにしました。
出来事？：ブルームバーグの報道によると、コロナウイルスの発生を抑制するために、インド経済は40年以上ぶりに本格的な縮小に向かう可能性があるという。


# 日本　17文
出来事　：シドニー 彼らは「ニュージーランド・ノマド」と呼ばれているが、それには理由がある。
出来事　：全国ラグビーリーグの「ニュージーランド・ウォリアーズ」は、コロナウイルスの大流行によりオーストラリアへの渡航が全面的に禁止されていたにもかかわらず、入国許可を得て、日曜日にニューサウスウェールズ州の小さな地方空港に到着する予定でした。
出来事　：14日間の隔離期間中は、州北西部のタムワースでトレーニングを行うことができますが、5月28日に予定されているシーズン再開後は、シドニーの北に位置するセントラルコーストに移動し、ほとんどの試合をこの地域で行うことになります。
出来事？：彼らは今のところ家族と離れており、NRLのシーズンが終わるまでニュージーランドに戻ることはできないでしょう。
出来事　：それは、今から約6ヶ月後の10月です。
出来事　：ウォリアーズの最高経営責任者であるキャメロン・ジョージは、現在の制限が緩和されれば、数カ月後には家族も一緒に来れるようになると期待している。
出来事　：彼によると、シーズン中は社内のウェルビーイング担当者がチームに残り、クラブはニュージーランドに戻った彼らの家族がサポートを受けられるようにするという。
主張？　：また、選手が早期に帰国しなければならなくなった場合、クラブは代替選手を申請することができます。
出来事　：今回のチームは、シーズン中にプレーする予定のチームです」とジョージはオーストラリアのAssociated Press社に語っています。
出来事　：しかし、個人的な理由で状況が変わる場合は、ケースバイケースですが、特に思いやりのある理由でNRLに申請することができます。
出来事　：パンデミックの影響で3月23日にシーズンが中断されるまで、NRLは2戦行われました。
出来事　：オーストラリアのメディアが土曜日に報じたところによると、NRLは修正されたスケジュールで20ラウンドのシーズンを予定しており、グランドファイナル・チャンピオンシップは10月25日に行われるとのことです。
出来事？：試合会場はまだ決定していませんが、すべてニューサウスウェールズ州で行われると予想されています。
出来事　：金曜日、クイーンズランド州政府は、州内のNRL3チームがニューサウスウェールズ州で試合を行うために国境を開放すると発表しました。
主張？　：現在、2つの州間の移動には制限があります。
出来事　：これにより、クイーンズランド州北部のブリスベンとゴールドコーストは、シドニーの隔離キャンプに入る必要がなくなり、シーズン再開前に家族と一緒に自宅で過ごすことができるようになりました。
出来事　：オーストラリアの各州では、パンデミックによる制限が緩和されており、日曜日の時点で全国のCovid19による死者数は95人と比較的少なく、新たな感染者も減少しています。


# 韓国　12文
出来事　：韓国銀行 yonhapincreased pressed to play more active role in the coronavirushit financial market 南朝鮮中央銀行は、社債や企業手形の購入など、流動性を供給するための例外的な措置を検討している。
出来事　：韓国銀行は木曜日に決定機関である金融政策委員会を開催し、基準金利の調整やその他の重要な金融措置の必要性を検討する予定であると当局は述べています。
出来事？：コビット19の流行による経済的影響が長期化し、緩和措置の必要性が継続しているにもかかわらず、市場の専門家は一般的に、中央銀行は今回、様子を見ながら金利を凍結するだろうと考えていました。
出来事？：大信証券のアナリスト、ゴン・ドンラク氏は、「今回、中央銀行は金利を凍結し、実質的に量的緩和とみなされるべき大幅な利下げとレポオペの影響を観察するのではないかと予想している」と述べた。
出来事　：先月、金融庁は緊急会合を開き、基準金利を50ポイント引き下げ、前例のない0.75％とした。
出来事　：それに続く緩和策として、北京銀行は先週、約5兆2500億ウォン（約42億円）の流動性を、現先取引（レポ取引）を通じて金融市場に供給した。
出来事？：不確実性は残っているが、流動性の逼迫は緩和の兆しを見せていると、kb証券のキム・サンフン氏は言う。
出来事？：韓国銀行は、少なくとも第1四半期の経済指標が出揃うまでは、重要な決定を控えることを好むかもしれません。
出来事？：しかし、一部の人々は、米国連邦準備銀行と比較して相対的に受動的であるBoksの政策ロードマップの有効性を疑問視している。
出来事　：先月、米国中央銀行は、適格社債を発行者から直接または流通市場で購入するための、一次市場企業信用枠と二次市場企業信用枠を発表しました。
出来事　：また、米国議会がCovid19に対処するための緊急財政資金法案を承認したことにより、中央銀行は企業にさらに4兆円を貸し付ける権限を与えられました。
出来事？：市場の状況が悪化した場合、韓国金融研究院のチャン・ミン上級研究員は、金融会社から社債を購入する間接的な方法として、特別目的会社への資金提供を検討することができると述べている。
```

ニュースで**出来事の文**が多いのは納得できるが、29文中27文（約93.1%）を占め、**極端に多すぎる**印象を受ける。

分類結果を手動で確認したところ、**39文中11文（約28.2%）の分類がエラーではないかと判断した。**

例えば、**出来事の文に分類された以下の文**は、**筆者とは別の人物が曖昧さを含む考え**を示しているため、**主張の文**だと考えられる。
```
出来事？：ブルームバーグの報道によると、コロナウイルスの発生を抑制するために、インド経済は40年以上ぶりに本格的な縮小に向かう可能性があるという。
```
また、**主張の文に分類された以下の文**は、「早期」という単語に曖昧さは残るものの、**確定的な規律や事実**を述べており、**出来事の文**だと考えられる。
```
主張？　：また、選手が早期に帰国しなければならなくなった場合、クラブは代替選手を申請することができます。
```

分類エラーが多い要因のひとつとして、分類モデルの**過学習**が考えられる。
つまり、IBM Debater Datasets の特徴を学習しすぎて、covid-19の記事に応用できていない可能性がある。
いつか読んだ文献（要調査）で、転移学習は5エポック前後で良い結果が出ることがあるとの記載があった。
予備実験では3エポックか5エポックかで96%の適合率が出ていたため、より少ないエポック数でより高い精度が出る可能性がある。

また、モデルの学習に用いた**IBM Debater Datasetsがニュース記事の分類に適していない可能性**も考えられる。
**IBM Debater Datasetsの文を目視で確認**し、ニュース記事にない特徴がないかを確認したい。

加えて、**コードのエラー**が原因である可能性も考えられる。
特に、pythonのforeach文でイテレータの順序が保証されているかを確認したい。
保証されていない場合、ラベルと文章との組が分類通りにリンクされていない可能性がある。

**特徴量**が二次元で記録できているため、**座標にプロットして傾向を掴む**のも有効かと考える。

いずれにせよ確認した記事の**母数が少ない**ため、上記の要因を確認した後に再び**100文**ほど分析したい。


## 3. 次回までに実施予定であること
- 卒論の目次作成
- 分類結果を吟味
- クラスタリングの実装
    - 出来事の文章の特徴量ベクトルを作成
    - 主張の文の特徴量ベクトルを作成
    - 3カ国の記事を結合して保存
    - [e-feature-array]を基に記事（行）をクラスタリング
    - 出来事の記事クラスタからnation-name;article-n;sentence-nで記事を特定
    - 指定した記事クラスタファイルの文を、cの[feature-array]でクラスタリング
    - 主張の文クラスタからnation-name;article-n;sentence-nで文とそのクラスタを特定
- 評価方法の検討
- 

## 4. メモ
- TODO
    - 全体的に
        - printデバッグを増やす
            - オリジナルのprint_debug()を作成
                - import
            - xqq君のjavaコードを参照
        - オプションでアルゴリズムを可変に
        - 後で何かやりたくなったときにできるように余分に処理しとく
        - こまめに記事をバックアップ
    - 主張と出来事の分類
        - process_01_train_classifier_as_claim_or_evidence.py
        - process_02_exe_classifier_as_claim_or_evidence.py
        - india-articles_process-01_classified-claim-or-evidence.txt
        - 日本記事を3か国の記事に変更
            - for with openではなく、複数のファイル名を指定して実行
                - 別にファイル名のtxtファイルを作成
                - 長くて指定が面倒なのでやっぱりfor with open
                    - no time
        - #を元にリストに格納
        - 分類
            - 時間かかるからpyにした方がいいかも
        - #e;feature-x;feature-y;sent-1#c;feature-x;feature-y;sent-2...\n のtxt
            - DeepL翻訳で10記事ほどチェック
            - 文頭、文末はシャープがないことに注意
        - ニュートラルも含めることを考えつつ
        - シャッフルを消す
            - 前処理前の記事との紐づけのため
            - 本当は必要
    - 出来事の文章の特徴量ベクトルを作成
        - process_03_articles_features_calculator.py
        - india-articles_process-03_calced-articles-features.txt
        - 出来事の文のみを結合
            - 一応主張、全文も作っておく
            - 文の間にスペースを挿入
        - SBERTに入れる
        - 文頭にarticle-n;[e-feature-array];[c-feature-array];[all-feature-array]#を追加
        - 記事にcが存在しない場合'-'を代入
        - 記事にeが存在しない場合'-'を代入
    - **主張の文の特徴量ベクトルを作成**
        - process_04_sentences_features_calculator.py
        - india-articles_process-04_calced-sentences-features.txt
        - #e:sent-1#c:sent-2...\n
        - S-BERTにsent-nを入れて特徴量を算出
        - article-n;[e-feature-array];[c-feature-array];[all-feature-array]#article-n;sentence-n;e;feature-x;feature-y;[feature-array];sent-1#article-n;sentence-n;c;feature-x;feature-y;[feature-array];sent-2...\n とする
            - 各文に特徴量を追加
            - 各文に番号を追加
            - #eのfeatureは不要だが、もしかしたら使うかも
        - txt保存
    - 3カ国の記事を結合して保存
        - process_05_nations_articles_concatenator.py
        - process-05_concatenated-nations-articles.txt
        - 国情報を付与
            - nation-name;article-n;[e-feature-array];[c-feature-array];[all-feature-array]#nation-name;article-n;sentence-n;e;feature-x;feature-y;[feature-array];sent-1#nation-name;article-n;sentence-n;c;feature-x;feature-y;[feature-array];sent-2...\n
    - [e-feature-array]を基に記事（行）をクラスタリング
        - process_06_articles_cluster_generator.py
        - クラスタごとに名前を付けて保存
            - process-06_generated-articles-cluster_n.txt
        - アルゴリズムはオプションで変更
            - ファイル名の末尾にアルゴリズム名
        - クラスタの粒度
    - ある記事のある文章から、似た文章とその文章が書かれた記事が参照できるか
        - 出来事の記事クラスタからnation-name;article-n;sentence-nで記事を特定
        - 主張の文のクラスタリング
        - 主張の文クラスタからnation-name;article-n;sentence-nで文とそのクラスタを特定
        - クラスタごとの主張の差異を分析
    - 出来事の記事クラスタからnation-name;article-n;sentence-nで記事を特定
        - process-07_find-articles-cluster-of-selected-sentence-info.sh
    - 指定した記事クラスタファイルの文を、cの[feature-array]でクラスタリング
        - process-08_sentences_cluster_generator.py
        - クラスタごとに名前を付けて保存
            - process-08generated-sentences-cluster_n.txt
        - 出来事の記事クラスタからnation-name;article-n;sentence-nで記事を特定
            - デバッグのため、後で実装
        - その記事クラスタファイルを開く
        - #で分割し、cの区分のみを1つのリストに格納
        - リストの要素を[feature-array]を基にクラスタリング
        - クラスタリング手法を変えやすいように
            - オプションで変更
            - 変更できるライブラリ
    - 主張の文クラスタからnation-name;article-n;sentence-nで文とそのクラスタを特定
        - process-09_find-sentences-cluster-of-selected-sentence-info.sh
    - 評価
        - 論文を読んで決める
    - まとめ
        - sent-1#sent-2#...\n
        - e;feature-x;feature-y;sent-1#c;feature-x;feature-y;sent-2...\n 
        - article-n;[e-feature-array];[c-feature-array];[all-feature-array]#e;feature-x;feature-y;sent-1#c;feature-x;feature-y;sent-2...\n
        - article-n;[e-feature-array];[c-feature-array];[all-feature-array]#article-n;sentence-n;e;feature-x;feature-y;[feature-array];sent-1#article-n;sentence-n;c;feature-x;feature-y;[feature-array];sent-2...\n
        - nation-name;article-n;[e-feature-array];[c-feature-array];[all-feature-array]#nation-name;article-n;sentence-n;e;feature-x;feature-y;[feature-array];sent-1#nation-name;article-n;sentence-n;c;feature-x;feature-y;[feature-array];sent-2...\n
        - process-06_generated-articles-cluster_n.txt
        - process-07_find-articles-cluster-of-selected-sentence-info.sh
        - process-08_sentences_cluster_generator.py
        - process-09_find-sentences-cluster-of-selected-sentence-info.sh
- 実装
    - process_01_train_classifier_as_claim_or_evidence.py
    - process_02_exe_classifier_as_claim_or_evidence.py
        - pip install simpletransformersのエラー
            - ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behavior is the source of the following dependency conflicts. flake8 4.0.1 requires importlib-metadata<4.3; python_version < "3.8", but you have importlib-metadata 4.8.2 which is incompatible
            - simpletransformers.classification がimportできない
            - 使用環境はpython 3.6.9
            - python3 -m pip3 install importlib-metadata==4.2.0
                - https://www.piwheels.org/project/importlib-metadata/#install
            - pip uninstall importlib-metadata
                - https://qiita.com/hatopoppoK3/items/1b8cc622e60a7907df25
            - コード上はimportできていないが、普通に実行できた
            - outputs/best_model -> outputs/
                - https://ichi.pro/tanjunna-toransufuxo-ma-toransufuxo-ma-moderu-o-shiyoshita-namaetsuki-enthithi-no-ninshiki-211430808920736
- 実行
    - 学習
        - エポック数10
        - 9m07s
        - 'mcc': 0.9917720493522194, 'tp': 444, 'tn': 948, 'fp': 3, 'fn': 2, 'auroc': 0.9999787808914855, 'auprc': 0.9999550894751484, 'eval_loss': 0.031835234991561136, 'acc': 0.9964209019327129
    - 分類
        - 1つの記事に4.434935569763184秒
