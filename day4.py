# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 13:21:50 2018

@author: HP
"""
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask (__name__)

@app.route ('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Halo mz! Udah day 4 nih yee!!!"

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['user name'] == 'admin':
        session['logged_in'] = True
    else:
        flash ('wrong password!')
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='127.0.0.1', port=5004)