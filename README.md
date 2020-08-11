# 卒論CI
卒業論文を効率的に執筆するためのCIパイプラインです。

# 機能一覧
ブランチにpushした`ブランチ名.docx`を**Travis CI**でチェックします。
- textlintによる文章の自動校正
- ファイルの更新と校正結果をslackに自動通知

# クイックスタート
1. [SlackとTravis CIを連携させて`.travis.yml`の[API TOKEN]を設定](https://qiita.com/nwtgck/items/17840855cb76f60fa1fe)
2. GitHubに新規ブランチを作成
3. 卒論ファイル`ブランチ名.docx`を先ほど作成したブランチへpushする
4. 結果をslackで確認 (Travis CIが自動で校正＆通知)