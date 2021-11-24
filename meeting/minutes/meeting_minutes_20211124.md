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

# 報告会 議事録 2021年11月24日

## 報告

### 片岡
- 公式の「大量」がどの規模か
- 分散処理可能

### 亀川
- 講義内で実験協力
    - 強制は禁止
    - 個人特定ができないように

### 志田
- 表の検算
    - 下1桁を足し算
- 第nの過誤に注意

### 土屋
- 

### 平山
- 

### 増岡
- 

### 松本
- freeコマンドでメモリリークの確認
    - gc.collect()でゴミ収集
- gpuのメモリのチェック
    - 別のシェルでnvidia-smi
        - 画面表示などは60MB程度
    - サーバーはtopというコマンドがオススメ
        - 表示しっぱなし
        - オプションで絞り込み
- 手法の章と実装の章は別

### モ
- 

### 原田
- 

## 気になったこと
- 加瀬先輩の面接予定合わせ
- 亀川君にpaperswithcodeを伝える
    - https://paperswithcode.com/datasets

## 業務連絡
- 疋田先輩が東京サーバーに上げてくれる
- 留学生が増えている
    - 1人保留、3人検討
- 院進
    - 中村研究課長から修了要件にTOEIC550
    - 逃げの1手はあるらしい
- 3年生面接
    - 5限
    - 11/30(火)
    - 12/02(木)予備日
    - m0でない3年生も是非
    - 1人2問ほど考えておいて
    - 東京サーバーに質問テンプレ
        - \20xx年度研究室資料\2017年度研究室資料\3年生面談
        - 研究室資料
- 1月は報告会を相談会に切り替える
- 8日の報告会で目次作成
    - 1日に作り方を伝達
- 
```
@channel 
来週、3年生の面接があります。
内部進学しないB4は任意参加になります。

11/30 (火)
12/02 (木)予備日
5限 (17:00-18:40) です。

参加者は1人2問ほど質問を用意してください。
東京サーバーの以下のアドレスに過去の質問集があります。参考にしてください。
\20xx年度研究室資料\2017年度研究室資料\3年生面談
\20xx年度研究室資料\2016年度研究室資料\面談
\20xx年度研究室資料\2015年度研究室資料\面談
\20xx年度研究室資料\2014年度\2014年度3年生配属面接

参考までに、スレッドに
\20xx年度研究室資料\2014年度\2014年度3年生配属面接\配属面接質問テンプレート.txt
と、片岡の就活で聞かれた質問集を添付しておきます。

- 企業・業界の志望理由
- 仕事の要点・自分に合っているか
- 5年10年後に社内で成し遂げたいこと
- 携わりたい製品
- 開発物・開発ツール・その問題点
- 関心分野・技術
- 身に着けたいスキルのためにしたこと
- 製品・サービスの良し悪しや改善点
- リーダー経験・開発での役割
- 研究内容
- 最も情熱を注いだこと
- 学業・サークル・バイトで得たこと
- 中学・高校・大学をどう過ごしたか
- できること・長所
- 趣味・特技
- 自由記述アピール

```

```
「eJoy Extention」
Youtubeで2カ国語の字幕を同時に翻訳できるChrome拡張機能。おすすめです。
字幕にカーソル合わせると動画を停止して単語の訳を表示してくれたりもします。
https://chrome.google.com/webstore/detail/ejoy-english-learn-with-m/amfojhdiedpdnlijjbhjnhokbnohfdfb
```

```
データセット探しで参考になったサイト
google dataset search
https://datasetsearch.research.google.com/
paperswithcode
https://paperswithcode.com/datasets
ieee-dataport
https://ieee-dataport.org/documents/covid-19-news-articles#files
```
