import json

with open('jawiki-country.json', 'r') as f:
    for line in f:
        loaded = json.loads(line)
        if loaded["title"] == "イギリス":
            print(loaded["text"])
            with open('UK.txt', 'w', encoding='utf-8') as g:
                g.write(loaded["text"])
            break