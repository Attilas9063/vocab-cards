# 存檔、讀檔：只有這個檔案可以直接讀寫 data/ 裡的檔案
import json

def save_cards(cards):
    with open("data/cards.json", "w", encoding="utf-8") as f:
        json.dump(cards, f, ensure_ascii=False, indent=4)

def load_cards():
    with open("data/cards.json", "r", encoding="utf-8") as f:
        cards = json.load(f)
    return cards


