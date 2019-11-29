# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect
from contact_model import Contact

app = Flask(__name__)
app.debug = True
app.secret_key = 'some_secret'

@app.route(r'/', methods=['GET'])
def contact_book():
    contacts = Contact.query().fetch()
    return render_template('contact_book.html', contacts=contacts)

@app.route(r'/add', methods=['GET', 'POST'])
def add_contact():
    if request.form:
        #Crear el contacto
        contact = Contact(name=request.form.get('name'), phone=request.form.get('phone'), email=request.form.get('email'))
        #Guardar el contacto
        contact.put()
    return render_template('add_contact.html')

@app.route(r'/contacts/<uid>', methods=['GET'])
def contact_details(uid):
    contact = Contact.get_by_id(int(uid))

    if not contact:
        return redirect('/', code=301)
    return render_template('contact.html', contact=contact)

@app.route(r'/update/<uid>', methods=['GET', 'POST'])
def update_contact(uid):
    contact = Contact.get_by_id(int(uid))
    if request.form:
        contact.name = request.form.get('name')
        contact.phone = request.form.get('phone')
        contact.email = request.form.get('email')
        contact.put()
        return redirect('/contacts/{}'.format(contact.key.id()))
    return render_template('update_contact.html', contact=contact)

@app.route(r'/delete', methods=['POST'])
def delete():
    contact_id = request.form.get('uid')
    contact = Contact.get_by_id(int(contact_id))
    contact.key.delete()
    return redirect('/contacts/{}'.format(contact.key.id()))