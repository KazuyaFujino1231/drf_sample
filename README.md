# お願い

インディゴ社外で利用する場合は作成者にお声がけいただけると嬉しいです。

誓って社外秘情報は載せていませんし、大した価値のないポジトリです。
でも、そんなものがどこかで使われるのなら教えてくれると嬉しいなってだけです。

# 環境構築手順

1. リポジトをリクローン
    ```bash
    git clone https://github.com/KazuyaFujino1231/drf_sample.git
2. ディレクトリを移動
    ```bash
    cd drf-sample
3. poetry installの実行
    ```bash
    poetry install
4. Dockerをビルド
    ```bash
    make build
5. Dockerを起動
    ```bash
    make up
6. 以下のリンクが開けたらOK
    http://localhost:8000/admin/login/?next=/admin/



# DBeaverのセッティング

DBクライアントツールが入っているなら省略可能

1. 以下のリンクからDBeaverをダウンロード
    https://dbeaver.io/

2. PostgreSQLへの接続を作成する
    DB名、ユーザー名、パスワードなどの設定値はdocker.envファイル参照
