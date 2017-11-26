## ループを回す準備
さて、そろそろお待ちかねの順次ダウンロードにとりかかるとしましょう。

### 1. 変数に置き換える
『陸軍の頭脳』の1枚のみの画像ダウンロードのコマンドをおさらいします。

```
wget 'https://ia800308.us.archive.org/BookReader/BookReaderImages.php?zip=/28/items/brainanarmyapop00wilkgoog/brainanarmyapop00wilkgoog_jp2.zip&file=brainanarmyapop00wilkgoog_jp2/brainanarmyapop00wilkgoog_0013.jp2' -O 0013.jpg
```

ダウンロードするごとに増えてほしい数字部分はどこでしょうか?さて、その部分をここでは `$i` と置きます(先ほど、入力しなくてよいと書いた `$`マークとはまた別の意味がありますが、これは後述します):

```
wget 'https://ia800308.us.archive.org/BookReader/BookReaderImages.php?zip=/28/items/brainanarmyapop00wilkgoog/brainanarmyapop00wilkgoog_jp2.zip&file=brainanarmyapop00wilkgoog_jp2/brainanarmyapop00wilkgoog_$i.jp2' -O $i.jpg
```

$から始まるものは変数と呼ばれるものです。変数とは代入のできる仮の文字と理解していただいて取り急ぎは結構です。今回の場合 `$i` で画像の番号を示そうとしています。変数 `i` に値を渡すには、`i=0013`を実行してから、コマンドを実行する必要があります。こうすることで0013が`$i`の部分を置き換えるのです。

### 2. echo コマンド
さて、ここで途中となりますが、 `echo` コマンドについて解説します。`echo`コマンドは引数として渡された文字列をそのままオウム返しするコマンドです:

```
 $ echo test
test
```

だからこだまを意味するエコー。
`echo`を使うと、自分が入力したコマンドが正しくコンピューターに伝わっているかどうかを確認することができます。

### 3. エスケープする
では、`echo`コマンドを使って、先ほど検討してみたコマンドに i=0013を渡して実行してみましょう:

```
$ i=0013
$ echo RESULT: wget 'https://ia800308.us.archive.org/BookReader/BookReaderImages.php?zip=/28/items/brainanarmyapop00wilkgoog/brainanarmyapop00wilkgoog_jp2.zip&file=brainanarmyapop00wilkgoog_jp2/brainanarmyapop00wilkgoog_$i.jp2' -O $i.jpg
RESULT: wget https://ia800308.us.archive.org/BookReader/BookReaderImages.php?zip=/28/items/brainanarmyapop00wilkgoog/brainanarmyapop00wilkgoog_jp2.zip&file=brainanarmyapop00wilkgoog_jp2/brainanarmyapop00wilkgoog_$i.jp2 -O 0013.jpg
```

惜しい。`-O 0013.jpg`はうまくいってるのに、 URLの部分が `$i` のまま残ってしまっています。

実はシングルくオーテーションマーク(')はくくられた部分について、「コマンド上の意味がある記号があっても、その意味を無視する」という意味があります。どうしてこんなややこしいものを今までつけていたかというと、実はパラメーターの区切りを意味する `&` マークもコマンドライン上、意味を持っているからです。「エスケープする」とは、この記号の持つ意味を無効化することを意味します。

エスケープには次の2種類があります。
#### 3.1. エスケープしたくない部分をシングルクオートから外す
```
$ i=0013
$ echo RESULT: wget 'https://ia800308.us.archive.org/BookReader/BookReaderImages.php?zip=/28/items/brainanarmyapop00wilkgoog/brainanarmyapop00wilkgoog_jp2.zip&file=brainanarmyapop00wilkgoog_jp2/brainanarmyapop00wilkgoog_'$i'.jp2' -O $i.jpg
RESULT: wget https://ia800308.us.archive.org/BookReader/BookReaderImages.php?zip=/28/items/brainanarmyapop00wilkgoog/brainanarmyapop00wilkgoog_jp2.zip&file=brainanarmyapop00wilkgoog_jp2/brainanarmyapop00wilkgoog_13.jp2 -O 0013.jpg
```
#### 3.2 シングルクォーテーションを使わず、エスケープしたい文字を\\(バックスラッシュ)で指定する
```
$ i=0013
$ echo RESULT: wget https://ia800308.us.archive.org/BookReader/BookReaderImages.php?zip=/28/items/brainanarmyapop00wilkgoog/brainanarmyapop00wilkgoog_jp2.zip\&file=brainanarmyapop00wilkgoog_jp2/brainanarmyapop00wilkgoog_$i.jp2 -O $i.jpg
RESULT: wget https://ia800308.us.archive.org/BookReader/BookReaderImages.php?zip=/28/items/brainanarmyapop00wilkgoog/brainanarmyapop00wilkgoog_jp2.zip&file=brainanarmyapop00wilkgoog_jp2/brainanarmyapop00wilkgoog_13.jp2 -O 0013.jpg
```

それぞれ一長一短がありますが、結果は同じなので、お好みのほうを利用してください。