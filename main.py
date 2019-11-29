# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from contact_model import Contact

app = Flask(__name__)
app.debug = True
app.secret_key = 'some_secret'

@app.route(r'/', methods=['GET'])
def contact_book():
    return render_template('contact_book.html')

@app.route(r'/add', methods=['GET', 'POST'])
def add_contact():
    if request.form:
        #Crear el contacto
        contact = Contact(name=request.form.get('name'), phone=request.form.get('phone'), email=request.form.get('email'))
        #Guardar el contacto
        contact.put()
    return render_template('add_contact.html')



