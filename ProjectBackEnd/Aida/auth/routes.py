from app import app
from app.models import *
from app import db
from flask import render_template,request,redirect,url_for,make_response
import os
 
loginData={
    'username':'aida',
    'password':'1409'
}

@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method=='POST':
        if request.form['username']==loginData['username'] and request.form['password']==loginData['password']:
            resp =make_response(redirect(url_for('admin_index')))
            resp.set_cookie('adminLoginStatus','beli')
            return resp
        else:
            return render_template('auth/login.html')
    return render_template('auth/login.html')
