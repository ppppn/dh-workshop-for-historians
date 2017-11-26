## 必要最小限を見極める

このまま、ウィルキンソンの『陸軍の頭脳』で話を続けましょう。画像のURLだけを取り出してみます。

```
https://ia800308.us.archive.org/BookReader/BookReaderImages.php?zip=/28/items/brainanarmyapop00wilkgoog/brainanarmyapop00wilkgoog_jp2.zip&file=brainanarmyapop00wilkgoog_jp2/brainanarmyapop00wilkgoog_0013.jp2&scale=4&rotate=0
```

もうお気づきでしょうが、この本をパブリックドメインで公開しているサイトは、『陸軍の頭脳』を0001.jpgから1つずつ数字を増やしていって画像を公開しています(`brainanarmyapop00wilkgoog_0013.jp`)。

本文書冒頭でパラメータについて少し述べましたが、このURLはパラメータを引き渡しています。`?`マークはパラメータの開始を示しています。`&`マークはパラメータの切れ目を示しています。パラメーターは`パラメータ名=値`という形式で記載されています。

URLを分析すると次のとおりです。
- ダウンロード受付用URL: `https://ia800308.us.archive.org/BookReader/BookReaderImages.php`
- パラメーター:
 1. `zip=/28/items/brainanarmyapop00wilkgoog/brainanarmyapop00wilkgoog_jp2.zip`
 2. `file=brainanarmyapop00wilkgoog_jp2/brainanarmyapop00wilkgoog_0013.jp2`
 3. `scale=4`
 4. `rotate=0`

ここからは経験が重要になってきますが、パラメーターのうち、1と2は "brainanarmy" とありますし、zipやfileという名前のパラメーターとして値が引き渡されていることから、どうやら必要そうですよね。
一方、3, 4ですが、scaleは倍率、rotateは回転なので、別になくてもダウンロードできそう、とあたりをつけてみます。というわけで、3, 4を外してダウンロードをもう一度試してみましょう:

```
$ wget 'https://ia800308.us.archive.org/BookReader/BookReaderImages.php?zip=/28/items/brainanarmyapop00wilkgoog/brainanarmyapop00wilkgoog_jp2.zip&file=brainanarmyapop00wilkgoog_jp2/brainanarmyapop00wilkgoog_0013.jp2' -O 0013.jpg
--2016-11-30 15:33:04--  https://ia800308.us.archive.org/BookReader/BookReaderImages.php?zip=/28/items/brainanarmyapop00wilkgoog/brainanarmyapop00wilkgoog_jp2.zip&file=brainanarmyapop00wilkgoog_jp2/brainanarmyapop00wilkgoog_0013.jp2
ia800308.us.archive.org (ia800308.us.archive.org) をDNSに問いあわせています... 207.241.228.18
ia800308.us.archive.org (ia800308.us.archive.org)|207.241.228.18|:443 に接続しています... 接続しまし た。
HTTP による接続要求を送信しました、応答を待っています... 200 OK
長さ: 922845 (901K) [image/jpeg]
`0013.jpg' に保存中

0013.jpg                  100%[==================================>] 901.22K   660KB/s    in 1.4s    

2016-11-30 15:33:07 (660 KB/s) - `0013.jpg' へ保存完了 [922845/922845]
```

予想通り、うまくいったようです。しかも、長さという部分に注目してください。前の105Kから901Kまでサイズが大きくなっています。どうやらscaleパラメーターの値によっては画像が縮小されて(荒くなって)ダウンロードされてしまうようです。場合によるかと思いますが、できるだけ解像度は高いほうがいいですよね。

パラメーターは必要最小限にしましょう。削りすぎても、ダウンロードに失敗するだけですし、失敗したことの確認は簡単です。