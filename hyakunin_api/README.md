# What is this?
これは、APIとは何か?を説明するために作った簡易百人一首表示Webアプリケーションです。

## Requirements
Ubuntuでのパッケージでは次が必要

- sqlite
- python-sqlite
- python3-bottle
- python3-requests

環境により、適宜読み替え

## Structure
```
database/create_db.txt  # SQLiteデータベース作成用テキストファイル
html/searchbox.html     # 検索ボックス用HTMLファイル
api_server.py           # 簡易APIサーバー
web_server.py           # 簡易Webサーバー
README.md               # 本ファイル
```

## How to create SQLite database file
### Craete file
次のコマンドで、データベース作成用テキストファイルを読み込み、SQLiteのデータベースファイルを作成する
```
sqlite3 database/hyakunin.db -init database/create_db.txt
```
```
-- Loading resources from create_db.txt
SQLite version 3.19.3 2017-06-08 14:26:16
Enter ".help" for usage hints.
sqlite>
```
と表示されていれば、テーブルとデータが作成されているはず。

### Test the file
データをテストする。
```
sqlite> select * from songs;
```
結果がズラーッと表示される。表示されたら、
```
.quit
```
で抜ける

## Run API server and web server
```
python api_server.py &
python web_server.py &
```

## Access API server
- http://localhost:10080/ にアクセスする
    - メッセージが表示される
- http://localhost:10080/song/1 にアクセスする
    - 百人一首の1番目の歌が出てくる
    - 1を1〜100の整数を入力するとその番号の歌が出てくる

## Access web server
1. http://localhost:8080/ にアクセスする
2. 検索窓に1〜100の整数を入力する
3. 結果が表示される 