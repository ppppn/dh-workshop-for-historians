# Git 講座 資料
全体的にざっくり。なんとなく理解できる状態にすることを優先。

## 最速で GitHub を使う
### GitHub に登録する
https://github.com/

### レポジトリを作成する
https://github.com/new

- Repository name: my-1st-repository
- Description: なし
- Public / Private: Public
- Initialize this repository with a README: オン
- Add .gitignore: None
- Add a license: None

→Create repository をクリック

### レポジトリに新しいファイルを追加する
#### ゼロからファイルを作成する
1. Create new file をクリック
1. 白紙ページが出るので何か書く
1. Commit new file のところの1行コメントで後で読み返したときに何をやったかわかるような内容を記載する
1. デフォルトの Commit directly to the master branch. が選択された状態を確認する
1. Commit new file をクリック
1. 新しいファイルがレポジトリに追加される

#### 既存のファイルをアップロードする
1. ファイルをドラッグアンドドロップする
1. Commit changes のところの1行コメントを書く
1. デフォルトの Commit directly to the master branch. が選択された状態を確認する
1. Commit changes をクリック
1. 選択したファイルがアップロードされ、レポジトリに追加される

### レポジトリのファイルを編集する
1. 編集したいファイルをGitHubで開く
1. 鉛筆マークを押す
1. 内容を編集する
1. 終わったら、Commit changes のところの1行コメントを書く
1. デフォルトの Commit directly to the master branch. が選択された状態を確認する
1. Commit changes をクリック
1. 変更がレポジトリに適用される

### 過去を振り返る
https://github.com/ppppn/dh-workshop-for-historians/blob/master/ri_oda/parser.py

1. History をクリックする
1. 以下のコミットをクリックしてみる
    - remove a line for testing
    - refactor code in tag replacing / fix bug in processing abstract in pa…  …
1. コードの歴史を確認する

# Git を本格的に使う
GitHub 上での作業を毎回やるのはわりとつらめ

[SSH の設定](howtossh.md) が完了していることを前提としているため、対応できていない場合は戻る。

## Git って何なの
[バージョン管理システム](https://ja.wikipedia.org/wiki/%E3%83%90%E3%83%BC%E3%82%B8%E3%83%A7%E3%83%B3%E7%AE%A1%E7%90%86%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0) の1つ。
だいたい書いてあるので、まずは wiki を読む。

## GitHub に公開鍵を登録する
https://github.com/settings/keys で id_rsa.pub の内容を登録する

## レポジトリを作成する
https://github.com/new

- Repository name: my-2nd-repository
- Description: なし
- Public / Private: Public
- Initialize this repository with a README: オフ
- Add .gitignore: None
- Add a license: None


## git clone する

`SSH` が選択されていることを確認し、`Quick setup` の下にあるテキストボックスの内容をコピーする

サンプル
```
git@github.com:${username}/my-2nd-repository.git
```

自分のPCで以下を実行する

```
$ cd ~
$ git clone git@github.com:${username}/my-2nd-repository.git
$ cd my-2nd-repository
$ pwd
```
最後のコマンドの結果、 `my-2nd-repository` で終わるパスが表示されていればOK。

# 考え方とか

## レポジトリの考え方には2つある
- ローカルレポジトリ: 手元の PC にあるレポジトリというイメージ
- リモートレポジトリ: 手元の PC にないレポジトリというイメージ(とりあえず GitHub のことと思って良い)

## コマンド add / commit / push / pull / clone
- add: あるファイルを今の状態で commit 予定と、マークする
    - add されていなければ、ディレクトリに新規ファイルや変更のあるファイルがあっても、git は知らんぷりをすると思っておいて良い
- commit: add された状態のファイルで(ローカル)レポジトリに変更を記録する

https://backlog.com/ja/git-tutorial/intro/intro1_4.html

- push: ローカルレポジトリへのコミット内容をリモートレポジトリに反映する
- pull: リモートレポジトリへのコミット内容をローカルレポジトリに反映する

https://backlog.com/ja/git-tutorial/intro/intro3_1.html
https://backlog.com/ja/git-tutorial/intro/intro3_3.html

- clone: ローカルレポジトリがない状態で、リモートレポジトリの内容をローカルに展開する

```
git clone https://github.com/ppppn/dh-workshop-for-historians.git
```

https://github.com/ppppn/dh-workshop-for-historians のレポジトリの内容がクローンされ、 dh-workshop-for-historians で見ることができる。
(これらのファイルは git の管理下に入っている)

## 作業ディレクトリの考え方
- ワークツリー: ファイルとして見えている内容。git で管理されているものとされていないものがある状態。
- インデックス: コミットするとマークされているファイルとその状態。git で管理されている。
- レポジトリ: 変更の記録がたまっている場所。

## コマンド status / log / diff
- status: ワークツリーの状態を確認する
- log: レポジトリへのコミットの記録を確認する
- diff: コミット間などの差分を取得する

# 作業の流れ

1. (特に共同作業の場合) git pull してリモートレポジトリへのコミット内容をローカルレポジトリに反映させる
1. ファイルを追加・変更していく
1. コミットしたいファイルについて git add して、コミットしたいファイルを git に伝える
1. git commit して、作成・変更したファイルをコミットする。そのときに、変更内容について、分かりやすくコメントを書く
1. git push してリモートレポジトリにコミット内容を反映させる

## 作業例

```
$ echo "My first line" > my-first-file.txt # ファイルに内容を書き込む
$ cat my-first-file.txt # 内容を表示する
My first line
$ git status # ローカルレポジトリの状態を確認する
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        my-first-file.txt

nothing added to commit but untracked files present (use "git add" to track)

###
# Untracked files(git により追跡対象となっていないファイル)に my-first-file .txt が入っている
# これはこのファイルが git の管理下に入っていないことを示す
###

$ git add my-first-file.txt # my-first-file.txt をコミット対象とし、git の管理下に入れる
$ echo $? # コマンドの結果を確認
0 # 0 と表示されたら成功
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   my-first-file.txt

###
# git の管理下に新しく入ってきたファイルとして認識された
###

$ git commit -m 'add my first file' # ローカルレポジトリにコミット
[master (root-commit) 7e8526b] add my first file
 1 file changed, 1 insertion(+)
 create mode 100644 my-first-file.txt

$ git push # github に push
Counting objects: 3, done.
Writing objects: 100% (3/3), 243 bytes | 243.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
remote: 
remote: Create a pull request for 'master' on GitHub by visiting:
remote:      https://github.com/ppppn/my-2nd-repository/pull/new/master
remote: 
To github.com:ppppn/my-2nd-repository.git
 * [new branch]      master -> master

# ここで、 github 上でレポジトリの状態を確認する

$ echo 'new line' >> my-first-file.txt # 新しい行を追加する
$ cat my-first-file.txt # 内容を確認
My first line
new line
$ git status # ワークツリーの状態を確認
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   my-first-file.txt

no changes added to commit (use "git add" and/or "git commit -a")
###
# my-first-file.txt はすでに git 管理下に入っている。
# このファイルは変更が加えられたと git が認識している
# だが、この段階ではレポジトリにコミットすべきとは認識されていない
###
$ git diff # 差分を表示
diff --git a/my-first-file.txt b/my-first-file.txt
index a63f21e..fab897e 100644
--- a/my-first-file.txt
+++ b/my-first-file.txt
@@ -1 +1,2 @@
 My first line
+new line
$ git add my-first-file.txt # コミット対象としてファイルを追加
$ echo $?
0
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   my-first-file.txt

###
# ファイルが変更され、かつ、コミット対象と認識している
###

$ git commit -m 'add new line'
[...]
$ git push
[...]
# github で確認する
# github 上でファイルを編集する
$ git pull # github上の変更をローカルレポジトリに取り込む
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
From github.com:ppppn/my-2nd-repository
   05675a3..c492584  master     -> origin/master
Updating 05675a3..c492584
Fast-forward
 my-first-file.txt | 1 +
 1 file changed, 1 insertion(+)
$ cat my-first-file.txt # 内容確認
My first line
new line
3rd line
$ git log # これまでのコミットログを確認
$ git log
commit c4925840124048373f5f92111dd3341fba3a1656 (HEAD -> master, origin/master)
Author: Akira Tanaka <ppppn@users.noreply.github.com>
Date:   Mon Oct 22 22:05:36 2018 +0900

    add third line

commit 05675a3df00c4d2cbe03bb64ac2b37e7c5f7b103
Author: Akira Tanaka <akira.tanaka.1897@gmail.com>
Date:   Mon Oct 22 22:05:05 2018 +0900

    add new line

commit 7e8526b6a45c06227ddff391bde2b08edfa25561
Author: Akira Tanaka <akira.tanaka.1897@gmail.com>
Date:   Mon Oct 22 21:57:27 2018 +0900

    add my first file
```

# (参考)Network を見る
Git ではブランチを切ることができる。

## よくある運用
master ブランチとは別に、ある機能の開発用にブランチ dev-hoge を切る。
新規に開発する機能のコードは dev-hoge ブランチにコミットしていくが、 master ブランチはそのままに残す(バグ取りとはかは別途行う)。

最終的に新機能の実装が完了し、テストも終わった時点で、 dev-hoge ブランチの変更内容を master ブランチに取り込み、本番に組み込む(マージ)。
逆に、 master ブランチの修正を適宜 dev-hoge ブランチに取り込むこともできる。

これにより、本番用の master ブランチの状態とは別に、新機能追加の作業環境を確保できる。

## プルリクエスト
ローカルレポジトリとリモートレポジトリの対応は n:m のため、自分が push/pull できるレポジトリなら、相互に反映させることが可能である。
ただ、自分が push できないレポジトリのファイルについて「こういう風に変更したらよりよくなるのに」という変更を push することはできない。
この時、プルリクエストを投げることで、そのレポジトリの所有者に pull してもらえるよう依頼(request)を出すことができる。
