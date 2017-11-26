## Windowsだけでやってみる
### 1. PowerShellを使う
最近のWindowsには、PowerShellというCUIが実は入っているのですが、これを使うと、Linuxを使わなくても、順次ダウンロードができます。

```
for ($i = 0; $i -lt 10; $i++) { Invoke-WebRequest -uri http://example.com/images/image-$i.jpg -outFile $i.jpg }
```

実は、`Invoke-WebRequest`というコマンドレットは別名が`wget`らしく、`Invoke-WebRequest`を`wget`に変えても動きます。
`for`の後ろの `( )` の中身は、`(初期設定; 継続条件; 1回終わるごとにやる処理)` で書かれています。
- 初期設定:  $i を0にセット
- 継続条件: $i が lt = "less than" 10
- 1回終わるごとにやる処理: $i を1つ増やす ($i = $i + 1と同じ)
PowerShellは非常にプログラミング的要素が強く、個人的には発想が面白いと思っています。
Cookieをどうやって付与するのかも調べはついているのですが、どうすればうまく解説できるのかはわからないので割愛。
ここまで読み進めてこられた人でWindows 10の環境があるなら、次の方法が~~まだ~~おすすめです。

### 2. Bash on Ubuntu on Windowsを使う
Windows 10にはWindowsの上でUbuntuを動かして、そこでCUI(ここまでの解説で利用してきたCUIのあれ)を動かすという、非常に変態的な機能が付いています。

導入方法は、[こちら](http://www.buildinsider.net/enterprise/wsl/01)を参照してください。

ほとんどここまでUbuntuを使って解説してきたものと同じです。

ただ、違うのは、例えば、WindowsのCドライブにアクセスするは /mnt/c に移動する必要がある点です。
```
$ cd /mnt/c
$ mkdir example-book
$ cd example-book
$ for i in `seq 1 9`; do wget http://example.com/images/image-$i.jpg -O $i.jpg; done
```
このコマンドを実行すれば、Cドライブ直下に`example-book`というフォルダができ、その中に、`1.jpg`から`9.jpg`という画像ファイルがあることに気づくでしょう。
これならば、今までの解説をLinuxなしでできます~~が、この記事執筆時点で、Bash on Ubuntu on Windowsはまだベータ版で動作が保証されているわけではありません。
表示が崩れるなどは日常茶飯事です。期待しないでください。~~

2017年10月のWindows 10 Fall Creators UpdateでBash on Ubuntu on WindowsはWindows Subsystem for Linuxと名称が変更され、正式な機能となりました。