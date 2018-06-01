# API講習会

## ゴール
- APIの概念を理解する
- APIの実体を理解する
- APIのメリデメを理解する
- 作る側は何に気をつけるべきか

. . .

※ だいたい全部ざっくり

# APIの概念を理解する

## APIとは何か

## APIとは約束である

自動販売機で飲み物を買う場面

を想像してください

## 自動販売機

1. お金を入れる
1. ボタンを押す
1. 飲み物を取り出す
1. (あれば)お釣りを取る

## Wikipedia

「広義の意味ではソフトウェアコンポーネントが互いにやりとりするのに使用するインタフェースの仕様」

## ソフトウェアコンポーネント
「ソフトウェアコンポーネントが互いにやりとりする」

## 自販機の場合

あなたも自販機もソフトウェアコンポーネント

----

あなた: パラメータを2つ(お金と飲み物の種類)与えるソフトウェア

自販機: 飲み物とお釣りをあなたに提供するソフトウェア

## インターフェイスの仕様
「使用するインタフェースの仕様」

## 旅行でこんな経験は?

. . .

- 「このバス、先払いなの?後払いなの?」

. . .

- 「このバス、前から乗るの?後ろから乗るの?」

. . .

どちらも仕様が決まってないから起きること

## APIとは約束である
「○○と△△というパラメータをください

そうしたら、私は××を返します」

## Wikipedia再び
「APIはソフトウェアライブラリと対応しているのが一般的である。...

----

...APIは「期待される挙動」を規定し説明するが、ライブラリはその規則群の「実際の実装」である。」

## 自動販売機
自動販売機の中身って興味ないですよね?

. . .

そういうことです

. . .

使う側からしたら関係がない

## プログラミング
ある意味、API同士を組み合わせてやるもの

. . .

```
>>> len(some_list)
3
```


## 開発者側から見ると
使う側に影響を与えなければ、どんな実装に変えても良い


# APIの実体を理解する

## コード書いてきました
2時間くらいで雑に書いたコード

## だいたいこんな感じ
[図](https://sequencediagram.org/index.html#initialData=C4S2BsFMAJAMGQRBkPoM9DKDIZIZBWDIfENAaDAKD0DOGQH4ZA2hmIFoA+AdUgCNBWhmMAWGYgLmkBxLQIl9AthmKAOhkBJDIEDIwEI2RMsQA8FCnSasO3fkOGAV+MAuylPLVFzNp17DA+dqAZCLwHl1AIIAFAJKGVvB47OX3L6gBEAQi6cAMoAigAygOGmwoCpRoCmingAdgD2wDDJAG6QAE7QAUHQYVGeeN7KchT5yiERFoAKvoA55po6KWnQmTnQZUZdToCrcoAbloDWDIAQKoDxDIDaDIBmDI3CgC6mgEb6VgwuFd0q7vVN2kmp6Vm51j2AFhGAXJ4LgPD6ABQAEgAqALLhAJRDs4u6svJHrjyNAiIzrs2h1cusADRVHqAKblAHtqgHsGQAwKjgAIYABxAAH0AM45A4AOjRAE9AOYMpkAoxFAA)

## デモやります
- DBを操作
- APIリファレンスを読む
- APIサーバーを操作
- Webサーバーを操作

## 解説します
- DBを解説
- APIサーバーを解説
- Webサーバーを解説
- HTTPリクエストを解説

# APIのメリデメを理解する

## メリット
- データが落ちない
- 加工しやすい形でデータが入手できる

## デメリット
- 操作しにくい
    - 検索ボックスに入れてパーンのほうが楽
- まぁ、そういうもんといえばそういうもん

# 作る側は何に気をつけるべきか

## DBで方向性が決まる
- 一旦テーブルを作ると、変更は難しい
    - 後からフィールドを足すとかは厳しい

## APIの変更は混乱を招く
- APIとは約束である
    - 「お約束とは異なる新しい判断」では困る 
- https://www.youtube.com/watch?v=xklmxmgaFWA

## UIの変更は実はどうってことない
- 取ってきたデータをどう表示するかだけ
- 「みやすい」「かっこいい」「かわいい」
    - すべてデータがちゃんとした形であればこそ

. . .

Twitterのクライアントはいっぱいあるけど

Twitterというサービスは1つですよね?

# 終

## 質疑応答