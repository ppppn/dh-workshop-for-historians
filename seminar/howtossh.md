# SSH でサーバーに接続する
## はじめに～SSH とは～
Windows や Mac を含めた OS では、コマンドプロンプトやターミナルを開いてコマンドを入力することで、手元のコンピューターの操作をすることが可能となります。
(知らなかったという方へ「できるんです」)

このコマンドをネットワーク越しに別のコンピューターに送り、そのコンピューターを操作可能にする技術の1つが SSH です。

SSH では、1. パスワードを使って認証する方法と、 2. 本人であることを証明し、本人しか持っていない(はずの)特別なファイル(秘密鍵)を使って、認証する方法との2つがあります。

この資料では、まず、環境の用意し、 1 のパスワードを使う方法でサーバーに SSH で接続します。
続いて、より便利な 2 の方法で接続するための準備をし、この方法で接続をします。

なお、環境構築については、独断と偏見で特定のソフトウェアにロックして話を進めます。特にこだわりがない場合は、そのまま進めてください。
一方、世の中には、複数のソフトウェアがあるので、好みのものがある場合はそちらを使っていただいてもかまいませんが、読み替えは各自適宜、お願いいたします。

## 環境用意
### Mac の場合
執筆者が Mac を使ったことがないので、すべて適宜「はず」を補ってください。
SSH クライアントがデフォルトでインストールされているため、ソフトウェアの追加は不要です。

ただ、 Windows ではとある事情から、 git をインストールする手順としています。
そのため、歩調を合わせるため、 git をインストールしておいてください。

手順は

https://qiita.com/furusin_oriver/items/974a7b7fb8c56ad88d6e

を参考にしてください。ググったら1番上に出てきたやつなので、内容が適切かどうかは不明です。

### Windows の場合
SSH クライアントは Git for Windows に同梱されているものを使います。

ターミナルソフトウェアには Cmder を使います。
実は Cmder にも SSH クライアントが同梱されているのですが、日本語の表示で問題が発生します。
Git for Windows の SSH クライアントを使うのはそのためです。

#### Git for Windows のインストール
https://git-scm.com/download/win より Git for Windows のインストーラーをダウンロードします。

インストーラーを開いて、インストールを開始します。次のポイントを除いて、基本的に Next で進んでください。

- Adjusting your PATH environment という画面では Use Git from Git Bash only を選択してください
- Configuring extra options という画面では、 Enable symbolic links にもチェックを入れてください

Install というボタンまで到達できればゴールです。
インストールが終わったら Finish で閉じてください。

#### Cmder の展開・設定
http://cmder.net/ の Download Mini より、 Cmder mini をダウンロードしてください。
(Full には Git for Windows が入っていますが、前掲の理由から使えないため)

1. ダウンロードした zip ファイルを適切な場所に展開してください。
おすすめは、 C:\Users\bin というフォルダを作って、そこに展開する方法です。
フォルダのパスにスペースが入らないように注意してください。初回起動時にエラーになります。

2. Cmder をダブルクリックして開いてください。そうすると、初回は何かファイルがコピーされているはずです。
(コピーされない場合は何かうまくいっていないので、 zip ファイルの展開からやり直してみてください。)

3. 右下に「≡」のボタンがあるためクリックし、 Settings をクリックしてください。

4. 左ペインよりStartup - Tasks とたどってクリックしてください。

5. 右ペインのAdd/refresh default tasks... をクリックし、 Add new tasks を選択してください。`{Bash:: Git bash}` が追加されたことを確認してください。

6. 再度左ペインより、 Startup を選択し、右ペインの Startup options の Specfied named task を選択し、プルダウンメニューから `{Bash:: Git bash}` を選択してください。
これで、 Cmder を開くたびに Git for Windows 同梱の bash が起動されます。

## パスワードで SSH 接続
ここまでの手順が正しく完了していると、Mac、Windows ともに同じクライアントが使用できる状況になっています。

パスワードで SSH 接続するにはターミナル(Mac)またはCmder(Win)を開いた状態で以下の通りコマンドを入力します

`ssh $username@$server -p $port`

`$username` には各自のユーザー名(ID)を代入してください。

`$server` には接続先のサーバーのIPアドレスまたはホスト名を入力してください。

サーバーによりポート番号が指定されている場合には `$port` にそれを代入してください。指定がない場合は SSH のデフォルトのポート番号 22 が使用されます。

コマンド中の `$` は変数を指します。

正しく指定で来ている場合、通常はパスワードの入力を要求されるはずなので、パスワードを入力します。
パスワード入力時は `*` なども表示されないので注意してください。
SSH でサーバーに接続できると、プロンプトが変わっていることから分かるかもしれませんが、念のため、正しくサーバーに接続できているかを以下の通り確認いたします。

```
$ uname -n
$ ip a
```

なお、コマンド行の先頭の `$` は特権ユーザーではない一般ユーザーで実行するという意味です。

パスワードを変更するには、以下のコマンドを入力してください。

```
$ passwd
```

## 鍵認証で SSH 接続
### おおまかな手順
鍵認証という方法を使うことで、パスワードなしでサーバーに接続することができます。

鍵認証は、非常にざっくりいうと、勘合と似たようなもので、公開鍵と秘密鍵という2つの要素で成り立ちます。

詳細は割愛しますが、鍵の取り扱いの説明のために、非常に簡単に仕組みを説明します。

暗号化の際は、公開鍵を使って、情報を暗号化します。
暗号の解読には、秘密鍵を使用します。

公開鍵と秘密鍵とはペアですが、公開鍵から秘密鍵を割り出すのは非常に困難なことが、この暗号方式の肝となります。

秘密鍵はアクセスする本人のみが保持するものです。「これを使えるということは本人に間違いない」となるので、他人には一切公開してはいけません。
公開鍵は人に見せても大丈夫なものです。

次項以降では、鍵認証で SSH 接続する方法を解説しますが、大まかな流れは以下の通りです。

1. まず、鍵のペアを作成します。
2. 作成した鍵ペアのうち、公開鍵をサーバーにコピーし、設定を実行します。
3. 最後に秘密鍵を利用して、サーバーへのアクセスをおこないます。

### 鍵ペアの作成
鍵ペアの生成は以下のコマンドでおこなえます。

```
ssh-keygen -b 4096
```

すると、次のメッセージが表示されます。`#` 以降の内容で進めてください。
(この手の手順について書かれたものでは、一般に `#` 以降はコメントで、実際には入力しないことを意味します)

```
$ ssh-keygen -b 4096
Generating public/private rsa key pair.
Enter file in which to save the key (/xxxx/.ssh/id_rsa):    # デフォルトのまま Enter
Created directory '/xxxx/.ssh'.
Enter passphrase (empty for no passphrase):                 # 秘密鍵を開くためのパスフレーズを設定。PC を紛失しない自信があれば、そのまま Enter で空のままでもOK。
Enter same passphrase again:                                # もう一度パスフレーズを入力。
Your identification has been saved in /xxxx/.ssh/id_rsa.
Your public key has been saved in /xxxx/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:oDki43maHUBqCu4VSbA7PGwZcGmf2HqNvcm6xY6oDmU xxxx@yourcomputer
The key's randomart image is:
+---[RSA 4096]----+
|xxxxxxxxx        |
|xxxxxxxxx        |
|xxxxxxxxx        |
|xxxxxxxxx        |
|xxxxxxxxx        |
|xxxxxxxxx        |
|xxxxxxxxx        |
|xxxxxxxxx        |
|xxxxxxxxx        |
+----[SHA256]-----+
```

ファイルが正しく作成されていることも確認しておきましょう。次のような感じであれば OK です。
```
$ ls -la ~/.ssh
total 16
drwxr-xr-x 1 Administrator 197121    0 9月  20 10:38 ./
drwxr-xr-x 1 Administrator 197121    0 9月  20 10:38 ../
-rw-r--r-- 1 Administrator 197121 3243 9月  20 10:38 id_rsa     # 秘密鍵
-rw-r--r-- 1 Administrator 197121  755 9月  20 10:38 id_rsa.pub # 公開鍵
```
`~` はユーザーのホームディレクトリです。Windows であれば、`C:\Users\$username\`、Mac だと `/Users/$username` あたりです。

### 公開鍵のサーバーへのコピー
次の手順でサーバーへ公開鍵をコピーします

```
scp ~/.ssh/id_rsa.pub $username@$server:/home/$username/ -P $port
```

`$` のやつはパスワードで SSH 接続したものと大体同じです。まだパスワードを要求されます。

サーバーにパスワードで SSH 接続してください。

サーバーで次の通りコマンドを実行してください。

```
$ uname -n      # 目的のサーバーのホスト名が表示されることを確認する
$ ip a          # 目的のサーバーのIPアドレスが表示されることを確認する
$ cd ~          # ホームディレクトリに移動する
$ pwd           # /home/$username と表示されることを確認する
$ mkdir .ssh    # ~/.ssh ディレクトリを作成する
$ cat id_rsa.pub >> .ssh/authorized_keys    # ~/.ssh/authorized_keys に公開鍵を追記する
$ ls .ssh/authorized_keys   # authorized_keys の情報が表示されることを確認する
$ chmod 600 .ssh/authorized_keys    # ~/.ssh/authorized_keys を本人以外読み書きが一切できないようにする
$ ls -la .ssh/authorized_keys
-rw------- 1 popo popo 775 Sep 19 17:53 .ssh/authorized_keys # -rw------- であることを確認する
$ exit  # SSH 接続から抜ける
```

### 公開鍵でサーバーへ接続
以下のコマンドで公開鍵を使った接続ができるようになります。
```
ssh $username@$server -p $port -i ~/.ssh/id_rsa
```

## (参考)接続設定の保存
クライアント側の ~/.ssh/config の例

```
Host server
  HostName ${ip_address}
  IdentityFile ~/.ssh/id_rsa
  User ${username}
  Port ${port}
```