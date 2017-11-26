### リハーサル、本番
ではループを回してみましょう。 for文というものでループを回すのですが、書式は次のとおりです:

```
for 変数 in 値1 値2 ...; do 実行したコマンド1; 実行したいコマンド2; ...; done
```

軽く動かしましょう:

```
$ for i in 1 2 3 4 5; do echo $i; done
1
2
3
4
5
```

`in`の後ろに先ほど書いてみた `seq` の結果を展開すれば、目的に近づけるのは一目瞭然ですね。これを叶えてくれるのがバッククオート(\`)です。普段はめったに使わない記号なので、どこにあるかが、わからないかと思いますが、日本語キーボードの場合、 `Shift + @` で出せます。バッククオートでくくられた部分はコマンドとして解釈され、出力結果で置き換えられます:

```
$ for i in `seq -w 0003 0010`; do echo $i; done
0003
0004
0005
0006
0007
0008
0009
0010
```

グッジョブ。では、リハーサルといきましょう:

```
$ for i in `seq -w 0009 0013`; do echo RESULT: wget https://ia800308.us.archive.org/BookReader/BookReaderImages.php?zip=/28/items/brainanarmyapop00wilkgoog/brainanarmyapop00wilkgoog_jp2.zip\&file=brainanarmyapop00wilkgoog_jp2/brainanarmyapop00wilkgoog_$i.jp2 -O $i.jpg; done
RESULT: wget https://ia800308.us.archive.org/BookReader/BookReaderImages.php?zip=/28/items/brainanarmyapop00wilkgoog/brainanarmyapop00wilkgoog_jp2.zip&file=brainanarmyapop00wilkgoog_jp2/brainanarmyapop00wilkgoog_0009.jp2 -O 0009.jpg
RESULT: wget https://ia800308.us.archive.org/BookReader/BookReaderImages.php?zip=/28/items/brainanarmyapop00wilkgoog/brainanarmyapop00wilkgoog_jp2.zip&file=brainanarmyapop00wilkgoog_jp2/brainanarmyapop00wilkgoog_0010.jp2 -O 0010.jpg
RESULT: wget https://ia800308.us.archive.org/BookReader/BookReaderImages.php?zip=/28/items/brainanarmyapop00wilkgoog/brainanarmyapop00wilkgoog_jp2.zip&file=brainanarmyapop00wilkgoog_jp2/brainanarmyapop00wilkgoog_0011.jp2 -O 0011.jpg
RESULT: wget https://ia800308.us.archive.org/BookReader/BookReaderImages.php?zip=/28/items/brainanarmyapop00wilkgoog/brainanarmyapop00wilkgoog_jp2.zip&file=brainanarmyapop00wilkgoog_jp2/brainanarmyapop00wilkgoog_0012.jp2 -O 0012.jpg
RESULT: wget https://ia800308.us.archive.org/BookReader/BookReaderImages.php?zip=/28/items/brainanarmyapop00wilkgoog/brainanarmyapop00wilkgoog_jp2.zip&file=brainanarmyapop00wilkgoog_jp2/brainanarmyapop00wilkgoog_0013.jp2 -O 0013.jpg
```

うまくいってそうですね。本番にいっても良さそうですね。

```
$ for i in `seq -w 0009 0013`; do wget https://ia800308.us.archive.org/BookReader/BookReaderImages.php?zip=/28/items/brainanarmyapop00wilkgoog/brainanarmyapop00wilkgoog_jp2.zip\&file=brainanarmyapop00wilkgoog_jp2/brainanarmyapop00wilkgoog_$i.jp2 -O $i.jpg; done
--2016-11-30 16:22:14--  https://ia800308.us.archive.org/BookReader/BookReaderImages.php?zip=/28/items/brainanarmyapop00wilkgoog/brainanarmyapop00wilkgoog_jp2.zip&file=brainanarmyapop00wilkgoog_jp2/brainanarmyapop00wilkgoog_0009.jp2
ia800308.us.archive.org (ia800308.us.archive.org) をDNSに問いあわせています... 207.241.228.18
ia800308.us.archive.org (ia800308.us.archive.org)|207.241.228.18|:443 に接続しています... 接続しまし た。
HTTP による接続要求を送信しました、応答を待っています... 200 OK
長さ: 139610 (136K) [image/jpeg]
`0009.jpg' に保存中

0009.jpg                  100%[==================================>] 136.34K   541KB/s    in 0.3s    

2016-11-30 16:22:16 (541 KB/s) - `0009.jpg' へ保存完了 [139610/139610]
# 以下略
```

あ、そうそう、途中でやめるときは Ctrl + C でどうぞ。これはコマンド全般に共通なので覚えておくとよいです。