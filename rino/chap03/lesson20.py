# -*- coding: utf-8 -*-

import json

def getEngland():

   json_path = "./input/jawiki-country.json"

   with open(json_path) as f:
      article_json = f.readline()

      while article_json:
         article_dict = json.loads(article_json)
         if article_dict["title"] == "イギリス":
            article_England = article_dict["text"]
         article_json = f.readline()

   return article_England

if __name__ == '__main__':
   article_England = getEngland()
   print(article_England)

   # 内容をtxtファイルに書き込み
   path_w = './output/lesson20.log'

   with open(path_w, mode='w') as f:
      f.write(article_England)
