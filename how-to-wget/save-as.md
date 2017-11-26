## 画像をダウンロードするときに好きな名前をつける
画像をダウンロードするときに名前をつけてしまいましょう。例えば、パブリックドメインになっている本のスキャンデータをコピーしたいときは、いい感じ名前をつけてダウンロードするのがいい戦略となります。

例えば、私が修士論文で使用した、ウィルキンソンの『陸軍の頭脳』の画像を普通にダウンロードしてみます(シングルくオーテーションでくくるのを忘れずに!理由は後述します):

```
$ wget 'https://ia800308.us.archive.org/BookReader/BookReaderImages.php?zip=/28/items/brainanarmyapop00wilkgoog/brainanarmyapop00wilkgoog_jp2.zip&file=brainanarmyapop00wilkgoog_jp2/brainanarmyapop00wilkgoog_0013.jp2&scale=4&rotate=0'
--2016-11-30 15:15:26--  https://ia800308.us.archive.org/BookReader/BookReaderImages.php?zip=/28/items/brainanarmyapop00wilkgoog/brainanarmyapop00wilkgoog_jp2.zip&file=brainanarmyapop00wilkgoog_jp2/brainanarmyapop00wilkgoog_0013.jp2&scale=4&rotate=0
ia800308.us.archive.org (ia800308.us.archive.org) をDNSに問いあわせています... 207.241.228.18
ia800308.us.archive.org (ia800308.us.archive.org)|207.241.228.18|:443 に接続しています... 接続しまし た。
HTTP による接続要求を送信しました、応答を待っています... 200 OK
長さ: 107702 (105K) [image/jpeg]
`BookReaderImages.php?zip=%2F28%2Fitems%2Fbrainanarmyapop00wilkgoog%2Fbrainanarmyapop00wilkgoog_jp2.zip&file=brainanarmyapop00wilkgoog_jp2%2Fbrainanarmyapop00wilkgoog_0013.jp2&scale=4&rotate=0' に保存中

BookReaderImages.php?zip= 100%[==================================>] 105.18K   462KB/s    in 0.2s    

2016-11-30 15:15:27 (462 KB/s) - `BookReaderImages.php?zip=%2F28%2Fitems%2Fbrainanarmyapop00wilkgoog%2Fbrainanarmyapop00wilkgoog_jp2.zip&file=brainanarmyapop00wilkgoog_jp2%2Fbrainanarmyapop00wilkgoog_0013.jp2&scale=4&rotate=0' へ保存完了 [107702/107702]
```

長大な名前がついてしまいました。しかもよく見ると、拡張子(.jpg)が取れてしまっているので、Windowsではうまく開けないでしょう。ダウンロード時にいい感じに名前を付けたくなるのもわかっていただけると思います。次に名前を指定してダウンロードします。

```
 $ wget 'https://ia800308.us.archive.org/BookReader/BookReaderImages.php?zip=/28/items/brainanarmyapop00wilkgoog/brainanarmyapop00wilkgoog_jp2.zip&file=brainanarmyapop00wilkgoog_jp2/brainanarmyapop00wilkgoog_0013.jp2&scale=4&rotate=0' -O 0013.jpg
--2016-11-30 15:19:11--  https://ia800308.us.archive.org/BookReader/BookReaderImages.php?zip=/28/items/brainanarmyapop00wilkgoog/brainanarmyapop00wilkgoog_jp2.zip&file=brainanarmyapop00wilkgoog_jp2/brainanarmyapop00wilkgoog_0013.jp2&scale=4&rotate=0
ia800308.us.archive.org (ia800308.us.archive.org) をDNSに問いあわせています... 207.241.228.18
ia800308.us.archive.org (ia800308.us.archive.org)|207.241.228.18|:443 に接続しています... 接続しまし た。
HTTP による接続要求を送信しました、応答を待っています... 200 OK
長さ: 107702 (105K) [image/jpeg]
`0013.jpg' に保存中

0013.jpg                  100%[==================================>] 105.18K   399KB/s    in 0.3s    

2016-11-30 15:19:13 (399 KB/s) - `0013.jpg' へ保存完了 [107702/107702]
```

0013.jpgという取り扱いやすい名前で保存されました。拡張子も取れていないし、0013.jpg, 0014.jpg, 0015.jpgと続き、順番に並んでくれるので、便利な形に保存できました。

wget コマンドでダウンロード後のファイル名を指定する方法は次のとおりです:
```
wget $URL -O $downloaded_filename
```