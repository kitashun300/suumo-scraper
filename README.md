# suumo-scraper

スーモの賃貸物件情報をPythonでスクレイピングし、CSV形式で出力するプロジェクトです。

## 概要
- 対象エリア：東京都世田谷区
- 対象ページ：検索結果の1〜3ページ
- 出力形式：表（pandas DataFrame）→ CSVファイル

## 取得項目
- 物件名
- 家賃
- 管理費
- 間取り
- 面積
- 最寄り駅・徒歩分数
- 築年数
- 詳細ページのURL

## 使用技術
- Python
- BeautifulSoup
- pandas
- Jupyter（初期開発環境）

## ファイル構成
- `bukken.py`：物件情報を取得しCSVに保存するスクリプト
- （※CSVファイルは後日追加予定）

## 今後の予定（任意）
- 出力CSVの追加
- 複数エリア対応
- データの可視化（平均家賃など）
