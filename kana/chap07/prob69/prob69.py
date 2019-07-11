#-*- coding: utf-8 -*-
#69. Webアプリケーションの作成

from flask import Flask, render_template, request
from mongodb import MongoDB


# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def post():
	if request.method == 'GET':
		return render_template('index.html')
	elif request.method == 'POST':	
		name = request.form.get('name','')
		area = request.form.get('area','')
		tag = request.form.get('tag','')

		if name + area + tag == "":
			return render_template('index.html')
		else:
			db = MongoDB()
			results = db.get_artist(name, area, tag)
		
			return render_template('index.html', results = results)
 
if __name__ == "__main__":
	app.run()