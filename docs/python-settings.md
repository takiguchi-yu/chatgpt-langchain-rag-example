## Getting Pyenv

pyenv で Python の複数バージョンを管理します。

### 前提環境

セットアップするときの前提環境です。

- OS: macOS Ventura 13
- Shell: Fish 3.6

### インストール方法

```sh
brew update
brew install pyenv
# インストールできたことを確認
pyenv --version
```

### シェルのセットアップ

```sh
set -Ux PYENV_ROOT $HOME/.pyenv
fish_add_path $PYENV_ROOT/bin
# 以下のコマンドで設定ファイルに設定を追加 ~/.config/fish/config.fish
pyenv init - | source
```

### 使い方

インストール可能なリストを確認する。

```sh
pyenv install --list
```

インストールする。

```sh
pyenv install 3.11.7
```

インストールしたバージョンを確認する。

```sh
pyenv versions
```

バージョンを切り替える。

```sh
# ユーザーアカウント全体に適用
pyenv global <version>
# 現在のシェルセッションのみ
pyenv shell <version>
# 現在のディレクトリ（またはそのサブディレクトリ）にいるときのみ
pyenv local <version>
```

### 参考資料

- https://github.com/pyenv/pyenv?tab=readme-ov-file#unixmacos

## Python

依存関係をインストールする。

```sh
pip install -r requirements.txt
```

インストール済みのライブラリのバージョンを確認する。

```sh
pip list
# ライブラリの詳細を確認する場合
pip show <ライブラリ名>
```
