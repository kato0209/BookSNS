# BookSNS
読書好きが繋がるというコンセプトのSNSアプリです。<br>
読んだ本の感想を投稿したり、他の人が書いた投稿を読んでコメントするなど、面白いと思った本の感想を他者と共有することができます。<br>
また、趣味が合うユーザーをフォローしたり、チャット機能を用いて会話をしたりなど、ユーザー同士での交流が可能です。<br>
<img src="{https://github.com/kato0209/BookSNS/assets/89386373/bcfae29c-3eea-488c-b309-fd484d41269b}" width="70%" />
![image](https://github.com/kato0209/BookSNS/assets/89386373/bcfae29c-3eea-488c-b309-fd484d41269b)<br>
![image](https://github.com/kato0209/BookSNS/assets/89386373/ba21c6c9-a4b8-4c7b-ac63-376eb1533643)

# URL
https://kato-aws-server.com/  <br>
※現在サーバー停止中

# 使用技術
●Django (Python)<br>
●Vue.js (JavaScript)<br>
●AWS<br>
●Rakuten Books API<br>

# AWS構成図
![GitHub_BookSNS](https://github.com/kato0209/BookSNS/assets/89386373/12cbafff-a767-43d7-9302-f56ecad15ed8)

# 機能一覧
●ユーザー登録、ログイン機能<br>
●パスワードを忘れたとき用の、メールアドレスを利用したパスワード変更機能<br>
●感想投稿機能<br>
  ○5段階評価機能<br>
  ○感想を投稿したい本をジャンルや、キーワード検索で探すことができる（検索結果の本一覧画面では、ページネーション機能あり）<br>
●コメント機能<br>
●チャット機能<br>
●ユーザー検索機能<br>
●投稿検索機能（投稿内容に対するキーワード検索や、検索した本に対する感想一覧を取得可能）<br>
●いいね機能(Ajax)<br>
●フォロー機能(Ajax)<br>
●ユーザープロフィール画像変更機能<br>
●読みたい本や、読み終わった本の管理機能<br>

●感想投稿の流れ↓
・感想を投稿したい本をキーワード or ジャンルで検索
![image](https://github.com/kato0209/BookSNS/assets/89386373/72483ea5-2926-44a0-ab7d-07bbe8a936a6)<br>
・対象の本を選択
![image](https://github.com/kato0209/BookSNS/assets/89386373/f1dfed96-a965-4854-b687-b53c0fd70a3d)<br>
・投稿
![image](https://github.com/kato0209/BookSNS/assets/89386373/b391682f-064b-4e42-a6f3-058326bc138d)<br>

●チャット機能
![image](https://github.com/kato0209/BookSNS/assets/89386373/f678cc87-27ef-47e4-a94e-e9e5b1059aa7)
