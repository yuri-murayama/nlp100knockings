#!/Users/zhangjiaying/.pyenv/versions/anaconda2-4.3.1/envs/py35/bin/python
#-*- coding: utf-8 -*-

# 参考 : https://qiita.com/goodboy_max/items/833d482827bf0efab45a
# 実行時コマンド(ローカルサーバー) : python -m http.server 8080 --cgi

import cgi
from pymongo import MongoClient
from pymongo import DESCENDING

print("Content-type: text/html")
print("<br>")

# 検索フォーム
print("""
<html>
    <head>
        <meta charset="utf-8">
        <title>検索結果</title>
    </head>

    <body>
        <h3> 再検索 </h3>
        <form action="http://localhost:8080/cgi-bin/nlp69.py" method="post">
            <p> アーティスト名(別名) : 
                <input type="text" name="name">
            </p>

            <p> タグ : 
                <input type="text" name="tags">
            </p>

            <p>
                <input type="submit" value="検索" name="submit">
                <input type="reset" name="reset">
            </p>
        </form>
""")

# cgi準備
form = cgi.FieldStorage()

# pymongo準備
client = MongoClient('localhost', 27017)

db = client.nlp64_database

# 検索条件
condition = {}
name_condition = {}
tags_condition = {}

if "name" in form:
    name_condition = {'$or' : [{'name':form.getvalue("name")}, {'aliases.name':form.getvalue("name")}]}

if "tags" in form:
    tags_condition = {'tags.value' : form.getvalue("tags")}

if len(name_condition)>0:
    if len(tags_condition)>0:
        condition = {'$and': [name_condition, tags_condition]}
    else:
        condition = name_condition
else:
    condition = tags_condition

result = db['nlp64_collection'].find(condition)

result.sort('rating.count', DESCENDING)

# 結果表示
print("<h3> 結果 </h3>")

if result.count()>10:
    print("検索結果が多いので先頭の20件を表示します<br>-----<br>")

for r in result.limit(20):
    print("アーティスト名(別名) : %s " %r['name'])
    if 'aliases' in r:
        aliase_lst = []
        for aliase in r['aliases']:
            aliase_lst.append(aliase['name'])
        print("(%s)" %", ".join(aliase_lst))            
    print("<br>")

    if 'area' in r:
        print("活動場所 : %s" %r['area'])
        print("<br>")

    if 'begin' in r:
        print("活動開始年 : %d年" %r['begin']['year'])
        print("<br>")

    if 'end' in r:
        print("活動終了年 : %d年" %r['end']['year'])
        print("<br>")

    if 'tags' in r:
        tag_lst = []
        for tag in r['tags']:
            tag_lst.append(tag['value'])
        print("タグ : %s" %", ".join(tag_lst))
        print("<br>")

    if 'rating' in r:
        print("レーティング : %s" %r['rating']['value'])
    
    print("<br><br>")

print("</body></html>")