## CUIで画像データを1枚だけダウンロードする

「千里の道も一歩から」ということで、早速、画像を1枚ダウンロードしてみましょう。

Ubuntuより「端末」を開いて、次のように入力してください(詳細は省略しますが、冒頭の$マークは一般権限を示していますので入力の必要はありません。`#`マーク以後はエスケープ(後述)していない限りコメントを示しているので、入力の必要はありません。

```
$ cd ~  #ホームディレクトリへ移動
$ mkdir -p test-download #テスト用ディレクトリの作成
$ cd test-download #作ったディレクトリへ移動 (cd のあとの文字列を途中まで入れてタブキーを押すと補完機能が働くので、几帳面にすべて入力する必要はありません。)
$ wget http://www.bun.kyoto-u.ac.jp/wp-content/uploads/2011/10/Rathaus.jpg #ダウンロード実行
```

実行結果がつぎのように表示されるとうまくいっています(以下、コマンド):

```
--2016-11-30 14:58:16--  http://www.bun.kyoto-u.ac.jp/wp-content/uploads/2011/10/Rathaus.jpg
www.bun.kyoto-u.ac.jp (www.bun.kyoto-u.ac.jp) をDNSに問いあわせています... 130.54.245.8
www.bun.kyoto-u.ac.jp (www.bun.kyoto-u.ac.jp)|130.54.245.8|:80 に接続しています... 接続しました。
HTTP による接続要求を送信しました、応答を待っています... 200 OK
長さ: 54006 (53K) [image/jpeg]
`Rathaus.jpg' に保存中

Rathaus.jpg         100%[===================>]  52.74K  --.-KB/s    in 0.05s   

2016-11-30 14:58:16 (1.06 MB/s) - `Rathaus.jpg' へ保存完了 [54006/54006]
```

スーパーキーを押して、"file" と入力すると「ファイル」というアイコンが出るのでクリックします。これはWindowsのエクスプローラー(ファイルを表示するもの)に相当するものです。

はじめに開かれるフォルダはWindowsでいうところのドキュメントフォルダのようなものです(Linuxではこれをホームディレクトリと呼びますので、以下、このように呼称します)。

さて、開かれたホームディレクトリからtest-downloadへ行くと Rathaus.jpg というファイルがないでしょうか?開いて見てください。そして、次のURLをクリックしてください: http://www.bun.kyoto-u.ac.jp/european_history/eh-enshu/

そうです、この Rathaus.jpg は西洋史研究室のホームページに使用されている画像なのです。画像のURLはChromeであれば、画像を右クリック→「画像のアドレスをコピー」で取得できます。

これで、1枚ずつではありますが、広く公開されている画像であれば、好きな画像をコマンドを使用してダウンロードする方法がわかりました。なにか好きな画像で試してみてください。