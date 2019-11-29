# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)
app.debug = True
app.secret_key = 'some_secret'

@app.route(r'/', methods=['GET'])
def contact_book():
    return render_template('index.html')


#este comando sirve para correr el proyecto en Flask. Una vez incluyamos app-engine esto pierde validez
if __name__ == '__main__':
    app.run()
