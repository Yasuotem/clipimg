# Clipimg
クリップボードの画像をwebpで保存してmdの画像リンクをクリップボードに保存

## インストール
uvを使います

```bash
uv tool install git+https://github.com/Yasuotem/clipimg.git
```

## コマンド
```bash
clipimg
```
カレントディレクトリにimagesフォルダを作成してクリップボード内の画像を1/2の大きさのwebpで保存
その後mdの画像のリンクをクリップボードに保存します。

## 使い方
1. print screen 等でクリップボードに画像を保存します
2. シェルで編集中のmdと同じフォルダで`clipimg`コマンドを実行
3. mdの画像リンクを入れたい場所で貼り付け

## zedのタスクに登録する例
tasks.json
```json
[
  {
    "label": "clipimg",
    "command": "clipimg",
    "reveal": "no_focus"
  }
]
```
keymap.json
```json
"ctrl-shift-v": [
  "task::Spawn",
  {"task_name": "clipimg"}
]
```
