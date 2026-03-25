# ccli

Atlassian Confluence Cloud をコマンドラインから操作する CLI ツール。

UNIX 哲学に基づき、パイプで他コマンドと組み合わせて使えるよう設計されています。

## 機能

- スペースの一覧・検索
- ページの検索・取得（HTML / JSON / テキスト形式）
- ページツリーの再帰的取得
- 添付ファイルの取得・保存

## インストール

```bash
# uv を使ってインストール
uv tool install ccli
```

## 設定

環境変数で認証情報を設定する（推奨）:

```bash
export CONFLUENCE_URL=https://your-domain.atlassian.net
export CONFLUENCE_USERNAME=you@example.com
export CONFLUENCE_API_TOKEN=your-api-token
```

API Token の発行: <https://id.atlassian.com/manage-profile/security/api-tokens>

または設定ファイルで設定する:

```bash
ccli config init
```

## 使い方

```bash
# スペース一覧
ccli spaces list

# スペース検索
ccli spaces search "Engineering"

# ページ検索
ccli pages search "Getting Started" --space DEV

# ページ取得（テキスト形式）
ccli pages get 123456789

# ページ取得（JSON形式、パイプで jq に渡す）
ccli pages get 123456789 --format json | jq '.title'

# ページ取得（添付ファイルも保存）
ccli pages get 123456789 --attachments --output-dir ./downloads

# ページツリーを再帰取得（JSON）
ccli pages tree 123456789 --format json | jq '.'

# ページツリー（深さ2まで、添付ファイル付き）
ccli pages tree 123456789 --depth 2 --attachments --output-dir ./downloads
```

## 開発

Python 3.11 以上と [uv](https://docs.astral.sh/uv/) が必要です。

```bash
git clone https://github.com/your-org/ccli.git
cd ccli
uv sync --all-extras
```

テスト実行:

```bash
uv run pytest
uv run pytest --cov=ccli --cov-report=term-missing
```

Lint / フォーマット:

```bash
uv run ruff check .
uv run ruff format .
uv run mypy src/
```

## ライセンス

MIT © magifd2
