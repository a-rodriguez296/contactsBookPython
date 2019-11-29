# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)
app.debug = True
app.secret_key = 'some_secret'

@app.route(r'/', methods=['GET'])
def contact_book():
    return 'Hola mundo'


if __name__ == '__main__':
    app.run()
