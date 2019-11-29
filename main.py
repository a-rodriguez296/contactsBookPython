# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True
app.secret_key = 'some_secret'

@app.route(r'/', methods=['GET'])
def contact_book():
    return render_template('contact_book.html')

@app.route(r'/add', methods=['GET', 'POST'])
def add_contact():
    if request.form:
        print(request.form.get('name'))
        print(request.form.get('phone'))
        print(request.form.get('email'))
    return render_template('add_contact.html')


#este comando sirve para correr el proyecto en Flask. Una vez incluyamos app-engine esto pierde validez
if __name__ == '__main__':
    app.run()
