from fastapi import FastAPI
import json
from logic.calculator import calculate_trade

app = FastAPI()

# JSON yükle
with open("data/items.json", "r") as f:
    items = json.load(f)


# 🔹 TEK ITEM ÇEK
@app.get("/item/{name}")
def get_item(name: str):
    return items.get(name, {"error": "item yok"})


# 🔹 TÜM ITEMLERİ ÇEK (SENİN İSTEDİĞİN BU)
@app.get("/items")
def get_all_items():
    return items


# 🔹 TRADE HESAPLA
@app.get("/trade")
def trade(item1: str, item2: str):

    # güvenlik kontrolü (çok önemli)
    if item1 not in items or item2 not in items:
        return {"error": "item bulunamadı"}

    value1 = items[item1]["value"]
    value2 = items[item2]["value"]

    result = calculate_trade(value1, value2)

    return {
        "you_gave": item1,
        "you_got": item2,
        "result": result,
        "value_gave": value1,
        "value_got": value2
    }