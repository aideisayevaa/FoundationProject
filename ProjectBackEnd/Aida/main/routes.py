# from re import M, T
from admin.routes import *
from app import app
from app.models import *
from flask import render_template,request,redirect



@app.route('/')
def index():
    logos=NavbarImg.query.all()
    profiles=ProfileImg.query.all()
    profiletxts=ProfileTxt.query.all()
    aboutheads=AboutHeading.query.all()
    skills=Skill.query.all()
    edus=Education.query.all()
    offers=Offer.query.all()
    infos=Counter.query.all()
    hobbys=Hobby.query.all()
    icons=NavbarIcon.query.all()
    socials=SocialIcon.query.all()
    endicons=ContactMe.query.all()
    menus=Portfoliomenu.query.all()
    links=Portfolio.query.all()
    tests=Testi.query.all()
    stars=Testimioanalstar.query.all()
    blogs=Blog.query.all()
    posts=AboutImg.query.all()
    ends=End.query.all()
    return render_template('main/index.html', logos=logos ,icons=icons, profiles=profiles,profiletxts=profiletxts,aboutheads=aboutheads,menus=menus, skills=skills, hobbys=hobbys, socials=socials,endicons=endicons,links=links,
    posts=posts,tests=tests,stars=stars,offers=offers,infos=infos,edus=edus,blogs=blogs,ends=ends)
@app.route('/admin/contactform', methods=['GET','POST']) 
def contactform():
   contactforms =Contact.query.all()
   if request.method=='POST':
      contactform=Contact(
   user_name=request.form['user_name'],
   user_email=request.form['user_email'],
   user_message=request.form['user_message'],
   user_subject=request.form['user_subject']

      )     
      db.session.add(contactform)
      db.session.commit()
      return redirect('/')
   return loginCheck (render_template('admin/contactform.html',contactforms=contactforms ))
   
@app.route("/admin/contactformdelete/<id>")
def contactformdelete(id):
   contactform =Contact.query.get(id)
   db.session.delete(contactform)
   db.session.commit()
   return redirect('/admin/contactform')



 
   