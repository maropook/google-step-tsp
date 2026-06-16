# How To Use
python -m http.server
http://localhost:8000/visualizer/build/default/

# Google STEP 2026: 巡回セールスマン問題チャレンジ
原著者: [Hayato Ito](https://github.com/hayatoito) (hayato@google.com)  
2020-2026年版: [Hugh O'Cinneide](https://github.com/hkocinneide)
(hughoc@google.com)、[Hiromu Ikeda](https://github.com/rombot98) (hiromu@google.com)、[Ayaka Kinoshita](https://github.com/oribe1115) (oribe@google.com)

## クイックリンク

- [スコアボード]

[スコアボード]:
  https://docs.google.com/spreadsheets/d/1uOhewb9KtMENU5AyLF8VcsyosQGOfkeh-Kka8M-DYcI/edit?usp=sharing&resourcekey=0-w2dZASN1e-X_gcl8vicB4Q
[github issues]: https://github.com/hayatoito/google-step-tsp/issues

## 問題の説明

この課題では、すべての巡回セールスマンが直面する基本的な問題、_巡回セールスマン問題_ (TSP) を解くアルゴリズムを設計します。TSP についてはオンサイトの授業で説明します。TSP は非常に有名な問題です。[Wikipedia](http://en.wikipedia.org/wiki/Travelling_salesman_problem) も参照してください。難しくなく理解できるはずです。

[Wikipedia](http://en.wikipedia.org/wiki/Travelling_salesman_problem) より引用:

> 巡回セールスマン問題（TSP）は次の問いを尋ねます: 都市のリストと各都市間の距離が与えられたとき、各都市をちょうど一度ずつ訪問して出発地に戻る最短経路はどれか？

## 課題

課題は GitHub にホストされています:
[https://github.com/hayatoito/google-step-tsp](https://github.com/hayatoito/google-step-tsp)

`git clone` でダウンロードできます:

```shellsession
git clone https://github.com/hayatoito/google-step-tsp
```

リポジトリには Python 2 ではなく Python 3 で書かれたサンプルスクリプトが含まれています。スクリプトを実行したい場合は Python 3 をインストールするのはあなたの責任ですが、スクリプトの実行は必須ではありません。

課題には N = 5 から N = 2048 まで、7 つの TSP チャレンジがあります:

| チャレンジ   | N（都市の数） | 入力ファイル  | 出力ファイル  |
| ----------- | -----------: | ----------- | ------------ |
| Challenge 0 |            5 | input_0.csv | output_0.csv |
| Challenge 1 |            8 | input_1.csv | output_1.csv |
| Challenge 2 |           16 | input_2.csv | output_2.csv |
| Challenge 3 |           64 | input_3.csv | output_3.csv |
| Challenge 4 |          128 | input_4.csv | output_4.csv |
| Challenge 5 |          512 | input_5.csv | output_5.csv |
| Challenge 6 |         2048 | input_6.csv | output_6.csv |

入出力ファイルのフォーマットは「データフォーマット仕様」セクションを参照してください。

### タスク

- アルゴリズムを設計・実装し、各 TSP を解くプログラムを書く。
- 各出力ファイル `output_{0-6}.csv` をプログラムの出力で上書きする。
- 各チャレンジについて、出力の _経路の長さ_ を [スコアボード] に入力する。言うまでもなく、経路は短いほど良い。

### ビジュアライザー

ビジュアライザーのデモページは[こちら](https://oribe.work/google-step-tsp/visualizer/build/default/)です。

課題にはあなたの解を可視化するヘルパー Web ページ `visualizer/build/default/index.html` が含まれています。ビジュアライザーにアクセスするにはローカルマシンで HTTP サーバーを起動する必要があります。どの HTTP サーバーでも構いません。Web サーバーの起動方法がわからない場合は、以下のコマンドを使用してください。コマンドを実行する前に、課題のトップディレクトリにいることを確認してください。

```shellsession
python -m http.server # Python 3 の場合
python -m SimpleHTTPServer 8000 # Python 3 をインストールしたくない場合
```

その後、ブラウザを開いて
[http://localhost:8000/visualizer/build/default/](http://localhost:8000/visualizer/build/default/) にアクセスしてください。

ビジュアライザーは Google Chrome のみでテストされています。ビジュアライザーの使用は任意です。課題を完了するためにビジュアライザーを使う必要はありません。問題の理解を助けるために提供されています。

GitHub Pages を有効にする方法については
[GitHub ヘルプ](https://help.github.com/articles/configuring-a-publishing-source-for-github-pages/)
を参照してください。

## データフォーマット仕様

### 入力フォーマット

入力は `N + 1` 行からなります。最初の行は常に `x,y` です。それに続く `N` 行は、i 番目の都市の座標を表し、`xi,yi`（`xi`、`yi` は浮動小数点数）の形式です。

```
x,y
x_0,y_0
x_1,y_1
…
x_N-1,y_N-1
```

### 出力フォーマット

出力は `N + 1` 行です。最初の行は "index" にする必要があります。それに続く `N` 行は都市のインデックスで、訪問順序を表します。

```
index
v_0
v_1
v_2
…
v_N-1
```

### 例（Challenge 0、N = 5）

入力例:

```
x,y
214.98279057984195,762.6903632435094
1222.0393903625825,229.56212316547953
792.6961393471055,404.5419583098643
1042.5487563564207,709.8510160219619
150.17533883877582,25.512728869805677
```

出力（解）の例:

```
index
0
2
3
1
4
```

これらのフォーマットはビジュアライザーの要件であり、正しくフォーマットされた CSV ファイルのみを入力として受け付けます。

## スケジュール

### 授業開始: 2026-06-12（金）17:00

「TSP」課題について説明します。

金曜日のアクションアイテム:

1. [スコアボード] の最初の列に名前を記入する。

2. このリポジトリを自分の GitHub にフォークする。

### コーディング期間: 2026-06-12（金）20:00 〜 2026-06-19（金）17:00

次の 2 週間、アルゴリズムを改善し、各チャレンジのスコアを [スコアボード] に手動で入力することが求められます。スコアは何度でも更新できます。より短い経路を見つけたときはすぐにスコアを更新することを強く推奨します。

第 7 回授業後も自由に提出・作業を続けてください。第 7 回授業でリーダーボードの結果を振り返りますので、成果を見せたい場合は授業開始時間までに提出してください！

## 課題に含まれるもの

問題の理解を助けるために、以下を含むいくつかのサンプルスクリプト/リソースが用意されています:

- `solver_random.py` - ランダムなサンプルソルバー。このランダムソルバーに負けることはないはずです。
- `sample/random_{0-6}.csv` - solver_random.py によるサンプル出力ファイル。
- `sample/sa_{0-6}.csv` - 別のサンプル出力ファイル。これも全員が上回ることを期待しています。ソルバー自体は意図的に含まれていません。
- `output_{0-6}.csv` - プログラムの出力でこれらのファイルを上書きしてください。
- `output_verifier.py` - 出力ファイルを検証し、経路の長さを表示します。
- `input_generator.py` - 入力ファイル `input_{0-6}.csv` の作成に使用した Python スクリプト。
- `visualizer/` - ビジュアライザーのディレクトリ。

詳細は意図的に省略されています。リポジトリの内容を理解するのはあなたの責任です。

## 行動規範

- 最善のアルゴリズムを競っているため、不正行為はしないでください:
- 支援を受けられるのは他の STEP 学生、メンター、または講師のみです。
- 他の人（友人、教授など）からの支援は受けないでください。
- サードパーティのライブラリを使用する際は最善の判断を行ってください。レビュアーがライブラリを理解するのが難しい場合、あなたが学べるはずの作業をやりすぎているかもしれません。
- もちろん、プログラミング言語が提供する組み込みライブラリを使用することは問題ありません。

## 開発のヒント

以下のヒントが役立つかもしれません:

- こまめにコミット・プッシュしましょう。小さなコミットはレビューしやすく、競合が起きにくいです。

- コードは一貫して整形されている必要があります。自信がない場合は適切なコードフォーマッターを使用してください。ツールが対応できる場合は手動でフォーマットしようとしないでください。

## よくある質問（FAQ）

この FAQ には過去の年の質問と回答が含まれています。一部の Q&A は今年には当てはまらない場合があります。

- Q. このドキュメントに誤字を見つけました。

- A. 練習として [プルリクエスト](https://help.github.com/articles/using-pull-requests/) を送るか、git に自信がない場合は [GitHub Issues] でイシューを立ててください。

- Q. 各チャレンジで同じコードを使わなければなりませんか？

- A. いいえ。

- Q. 使用できるマシンリソースに制限はありますか？複数のマシンを使えますか？アルゴリズムを 24 時間実行できますか？

- A. 制限はありません。使えるマシンリソースを何でも使用できます。

- Q. このドキュメントとスコアボードが公開されているようです。これは意図的ですか？

- A. はい。私は透明性を重視しています。懸念がある場合はお知らせください。ご意向を尊重します。機密情報は入力しないでください。

- Q. 他の学生のリポジトリを見ることができますか？

- A. はい。何も隠そうとしないでください。すべてはオープンであるべきです。学生間でアイデアを交換したり、アイデアを借用することは問題ありません。

## 謝辞

この課題は [Coursera の Discrete Optimization Course](https://www.coursera.org/learn/discrete-optimization) から強くインスパイアされています。
