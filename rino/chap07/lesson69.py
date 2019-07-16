# -*- coding: utf-8 -*-
from flask import Flask, request
from pymongo import MongoClient, DESCENDING

client = MongoClient('localhost', 27017)
db = client.artist_database
collection = db.artist_database
app = Flask(__name__)

def printArtist(info_list):
    print_string = ""
    for info in info_list:
        for k, v in info.items():
            print_string += "{}:{}<br>".format(k,v)
        print_string += "<br>"
    return print_string

def searchArtist(name, alias, tag):
    info_list = []
    info_col = collection.find({'$or' : [{'name': name},
                                         {'aliases.name': alias},
                                         {'tags.value':tag}]}).sort([('rating.count', DESCENDING)])

    for c in info_col:
        info_list.append(c)

    if info_list == []:
        string = "該当なし"
    else:
        string = printArtist(info_list)
    return string


@app.route("/", methods=["GET", "POST"])
def searchArtistDB():
    if request.method == "GET":
        return """

        <h1>言語処理100本ノック 69</h1>
        検索条件に合致するアーティストの情報を表示します。<br><br>

        <form action="/" method="POST">

        <p>アーティスト名:<br>
        <input name="artist"></input></p>

        <p>アーティストの別名:<br>
        <input name="aliases"></input></p>

        <p>タグ:<br>
        <input name="tag"></input></p>

        <p><input type = "submit" value = "検索" /></p>

        </form>"""

    else:
        return """
        {}""".format(searchArtist(request.form["artist"], request.form["aliases"], request.form["tag"]))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)
