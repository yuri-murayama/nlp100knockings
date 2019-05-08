import json

with open('jawiki-country-EU.json', 'r') as f:
    lines = f.read().split('\n')
    for line in lines:
        if "Category" in line:
            print(line)
