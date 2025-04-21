import json
with open("test.json", "r", encoding="utf-8") as f:
    data = json.load(f)

del data[0]
print(data[0])