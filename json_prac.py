import json

# 讀取 JSON 檔案
with open("test.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 取出第一筆資料的 name 欄位
first_name = data[0]["eng_sen"][0]
print(first_name)
