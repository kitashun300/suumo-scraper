#!/usr/bin/env python
# coding: utf-8



import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# データ格納用リスト
data = []

# 1〜3ページ分を繰り返し取得
for page in range(1, 4):
    url = f'https://suumo.jp/chintai/tokyo/sc_setagaya/?page={page}'
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.select('.cassetteitem')  # 物件ブロックの取得

    for item in items:
        try:
            title_tag = item.select_one('.cassetteitem_content-title')
            title = title_tag.text.strip() if title_tag else ""

            rent_tag = item.select_one('.cassetteitem_other-emphasis')
            rent = rent_tag.text.strip() if rent_tag else ""

            fee_tag = item.select_one('.cassetteitem_price--administration')
            fee = fee_tag.text.strip() if fee_tag else ""

            floor_plan_tag = item.select_one('.cassetteitem_madori')
            floor_plan = floor_plan_tag.text.strip() if floor_plan_tag else ""

            area_tag = item.select_one('.cassetteitem_menseki')
            area = area_tag.text.strip() if area_tag else ""

            access_tag = item.select_one('.cassetteitem_detail-text')
            access = access_tag.text.strip() if access_tag else ""

            age_tag = item.select_one('.cassetteitem_detail-col')
            age = age_tag.text.strip() if age_tag else ""

            url_tag = item.select_one('a.js-cassette_link_href')
            detail_url = "https://suumo.jp" + url_tag.get('href') if url_tag else ""

            # 1件分を辞書として追加
            data.append({
                "物件名": title,
                "家賃": rent,
                "管理費": fee,
                "間取り": floor_plan,
                "面積": area,
                "最寄り駅": access,
                "築年数": age,
                "URL": detail_url
            })

        except Exception as e:
            print("データ取得時にエラー:", e)

    time.sleep(1)  # サーバー負荷対策

# pandasで表に変換
df = pd.DataFrame(data)

# 表示
print(df)

# CSVとして保存
df.to_csv("suumo_bukken_setagaya.csv", index=False)




