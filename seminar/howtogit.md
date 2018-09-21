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

表示される create a new repository on the command line に従って作業してみる
→GitHubで直接、作業した内容と同じことができる。

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

## 作業ディレクトリの考え方
- ワークツリー: ファイルとして見えている内容。git で管理されているものとされていないものがある状態。
- インデックス: コミットするとマークされているファイルとその状態。git で管理されている。
- レポジトリ: 変更の記録がたまっている場所。

## コマンド status / log / diff
- status: ワークツリーの状態を確認する
- log: レポジトリへのコミットの記録を確認する
- diff: コミット間の差分を取得する

# 作業の流れ

1. (特に共同作業の場合) git pull してリモートレポジトリへのコミット内容をローカルレポジトリに反映させる
1. ファイルを追加・変更していく
1. コミットしたいファイルについて git add して、コミットしたいファイルを git に伝える
1. git commit して、作成・変更したファイルをコミットする。そのときに、変更内容について、分かりやすくコメントを書く
1. git push してリモートレポジトリにコミット内容を反映させる

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
