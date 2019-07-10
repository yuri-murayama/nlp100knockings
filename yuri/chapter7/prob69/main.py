from flask import Flask, render_template, request
from prob69 import find_artists

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        name = request.form['name']
        area = request.form['area']
        tag = request.form['tag']      
        posts = find_artists(name, area, tag)
        return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run()