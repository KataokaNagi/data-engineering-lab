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

# 週次報告書 2021年04月24日
AL18036 片岡 凪

## 今回の報告会までに実施する予定だったこと
- 報告書
- 論文調査
    - XAIの応用技術？
        - 何を説明したいか
        - 具体的なモデルの具体的なXAI手法
    - タグ分類？
    - その他、趣味や既習事項に関連するもの
    - これまでの報告会のメモを眺めてみる
- hand's on ML

## 実施内容

### Youtubeのデータセットの調査
新規の投稿者が反映されるリコメンド機能に少し関心があったため、

- [個人が収集したYoutubeのメタ情報](https://qiita.com/myaun/items/7e0dd7f3f9d9d2fef497)
- https://www.dsk-cloud.com/blog/useful-data-set-formachine-learning
    - YouTube-8M Dataset
        - Google の研究チームが公開している動画データセットで、700万件もの動画が公開されており4,800件のナレッジグラフのエンティティがタグ付けされています。動画データは、TensorFlowファイルとしてダウンロードできます。
    - YouTube-BoundingBoxes Dataset
        - YouTube-8M Dataset と同じく、Google が公開している動画データセットです。一般公開されているYouTubeビデオから抽出された、約38万の15-20ビデオセグメントで構成された動画データが約24万件公開されています。オブジェクトを自動的に選択でき、編集や後処理を行うことなく使用できます。

### 【CEDEC2019】ゲーム開発・運用における機械学習活用の現状と未来
by [モリカトロンAIラボ](https://morikatron.ai/2019/10/cedec2019_game_and_machinelearning/)  
  
研究外でデジタルゲームについて調査していたところ、MLを多く紹介する記事を見つけた。具体的なXAIを適用する具体的なMLモデルを探していたため、この中から選択して詳しくリサーチすることとした。どの技術も興味深いが、ゲーム以外に広く適用可能な技術として逆強化学習について詳しくリサーチする。

- 自動プレイによるテスト
- **強化学習**や**遺伝的アルゴリズム**によるバランス調整
- 入力ログの学習
- 手動テストの学習
- キャラのカメラ情報の**模倣学習、逆強化学習**
    - ロボットにも応用
- おもしろさのQA
    - アイテムの使用頻度など、つまらない要素の学習
    - カードゲームのパターン爆発のNN対応
    - 緊張度の学習
- **能動学習**や**転移学習**によるチート対策

### 上を基にしたテーマのアイディア
別ファイルで詳解するが、**逆強化学習（Inverse Reinforcement Learning）は、入力する優秀な行動について、その行動を超える優秀さをもつ行動を生むことができない。**この問題は、**逆強化学習とXAIを組み合わせる**ことで改善できるのではないかと考えた。XAIを用いることで、入力する優秀な行動に近づいたときに強く働いた報酬の特徴量を特定し、その特徴量の重要度を入力する優秀な行動の特徴量よりも上げることで性能の改善が見込めると考える。  
  
また、**逆強化学習と転移学習を組み合わせる**ことで、異なる分布同士の入力する優秀な行動を用いて、様々な状況にロバストに対応できる報酬の学習ができるのではないかと考えた。

### アイディアを基に論文調査
各単語の組み合わせについて、Google Scholorで2017年以降（一部設定し忘れがある）の論文一覧の1ページ目に目を通し、以下にまとめた。ヒットしなかった組み合わせは、相性の悪い組み合わせであるか、新規性のあるものであるかのいずれかであり、詳しく吟味する必要がある。今回読んだのは太字の2本で、逆強化学習と転移学習、転移学習とXAIの組み合わせについてより一般に捉えていそうな論文である。

- 逆強化学習＋転移学習
    - 英語ヒットなし
    - [複数環境におけるエキスパート軌跡を用いたベイジアン逆強化学習 転移可能な報酬の推定に向けたアプローチ](https://www.jstage.jst.go.jp/article/tjsai/35/1/35_G-J73/_article/-char/ja/)
        - 目的が同一の、異なるデモンストレーションの情報を転移
        - ベイズ逆強化学習問題
        - マルコフ連鎖モンテカルロ法
    - [複数のダイナミクス下でのデモンストレーションによる転移可能な逆強化学習](https://www.jstage.jst.go.jp/article/pjsai/JSAI2020/0/JSAI2020_2J6GS201/_article/-char/ja/)
        - 目的が同一の、異なるデモンストレーションの情報を転移
        - 最大エントロピー強化学習
    - [**逆強化学習を用いた転移可能な報酬関数の推定**](https://www.jstage.jst.go.jp/article/pjsai/JSAI2016/0/JSAI2016_3D3OS30a2/_article/-char/ja/)
- 転移学習＋XAI
    - [The design and implementation of Language Learning Chatbot with XAI using Ontology and Transfer Learning](https://arxiv.org/abs/2009.13984)
    - [Xai Language Tutor–A Xai-Based Language Learning Chatbot Using Ontology and Transfer Learning Techniques](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3732751)
    - [**A Visual Analytics Framework for Explaining and Diagnosing Transfer Learning Processes**](https://www.semanticscholar.org/paper/A-Visual-Analytics-Framework-for-Explaining-and-Ma-Fan/574a685e1bedc020987d6551ebc7580fbab3355f)
    - [Knowledge-based transfer learning explanation](https://arxiv.org/abs/1807.08372)
    - 日本語ヒットなし
- 逆強化学習＋XAI
    - 英語ヒットなし
    - 日本語ヒットなし
- 強化学習＋XAI
    - [Explainability in deep reinforcement learning](https://www.sciencedirect.com/science/article/pii/S0950705120308145)
    - 日本語ヒットなし
- 逆強化学習＋転移学習＋XAI
    - ヒットなし

## 次回までに実施予定であること
- 上述とは別の関心分野
    - データマイニング＋ML
    - DB＋ML
    - サーバー＋ML
- 気になった論文
    - 上述の論文
        - その他応用例も
    - [説明可能な AI (XAI)](https://www.jstage.jst.go.jp/article/jsimconf/80/0/80_51/_article/-char/ja/)
- テーマを考える
    - 前回のサジェストの質向上など
<!-- - Youtubeの暴言、指示
    - 動的な教師
        - 半教師？
    - そもそもMLいる？ -->
- hand's on ML
    - スライド作成
