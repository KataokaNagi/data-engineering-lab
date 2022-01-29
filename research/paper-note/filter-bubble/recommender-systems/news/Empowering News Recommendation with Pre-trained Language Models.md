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

# 論文要約 『Empowering News Recommendation with Pre-trained Language Models』

- [1]C. Wu, F. Wu, T. QiとY. Huang, 「Empowering News Recommendation with Pre-trained Language Models」, arXiv:2104.07413 [cs], 4月 2021, 参照: 2022年1月28日. [Online]. Available at: http://arxiv.org/abs/2104.07413
- 20220128参照


<!-- -------------------- -->

## 概要
- パーソナライズド・ニュースレコメンデーション
    - ニュース記事
        - には通常リッチなテキストコンテンツが含まれる
        - 正確なニュースモデリングが重要
        - 既存のニュース推薦
            - 伝統的なテキストモデリング手法に基づいてニューステキストをモデル化
            - ニューステキストに含まれる深い意味情報をマイニングするためには最適ではない
        - 事前に学習された言語モデル（PLM）
            - 自然言語理解に強力
            - 可能性を秘めている
        - PLMがニュース推薦に適用されたことを示す公的な報告書はない
            - ほんとう？
    - 本論文
        - 学習済みの言語モデルを用いてニュース推薦を強力に行う
        - 単言語および多言語
        - Microsoft Newsプラットフォームに導入
            - 大きな利益

<!-- -------------------- -->

## 図表
- 普通のフレームワーク
- PLMのフレームワーク
    - エンコーダーをPLMに
    - クリックした過去の埋め込みからユーザの埋め込みを作成
    - 新規の埋め込みと比較
- データセットの詳細
    - MIND
    - Multilingual
        - User
        - News
        - Impression
        - Click Behavior
- MINDで比較
    - EBNR
    - NAML
    - NPA
    - LSTUR
    - NRMS
        - それぞれBERT, RoBERTa, UniLM
    - NRMS-UniLMが最も優れている
- Multilingualで比較
    - 同じようなモデル
    - NRMS-InfoXLMが最も優れている
- BERTを変えて比較
    - BERT-baseがAUCトップ
- プーリングを変えて比較
    - CLS, AVEよりAttentionの使用が優れている
- NRMSに比べNRMS-UniLMはかなり凝集、乖離している

<!-- -------------------- -->

## はじめに
- 

### 
- 

### 
- 

### 
- 

<!-- -------------------- -->

## 
- 

### 
- 

### 
- 

### 
- 

<!-- -------------------- -->

## 
- 

### 
- 

### 
- 

### 
- 

<!-- -------------------- -->

##
- 

### 
- 

### 
- 

### 
- 

<!-- -------------------- -->

## おわりに
- 

<!-- -------------------- -->

## 片岡所感
- BERTでないNRMS-UniLMがトップ
    - 自分の研究で使いにくい

<!-- -------------------- -->

## 重要ピックアップ
- 
