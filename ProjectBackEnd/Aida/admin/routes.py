
from app import app
from app.models import *
from app import db
from flask import render_template,request,redirect
from flask import url_for
import os
# from flask_bcrypt import Bcrypt
def loginCheck(param):
    adminLoginStat = request.cookies.get('adminLoginStatus')
    if adminLoginStat=='beli':
        return param
    else:
               return redirect(url_for('login'))

@app.route('/admin')
def admin_index():
    logos=NavbarImg.query.all()
    icons=NavbarIcon.query.all()
    profiles=ProfileImg.query.all()
    profiletxts=ProfileTxt.query.all()
    aboutheads=AboutHeading.query.all()
    skills=Skill.query.all()
    hobbys=Hobby.query.all()
    infos=Counter.query.all()
    offers=Offer.query.all()
    edus=Education.query.all()
    socials=SocialIcon.query.all()
    endicons=ContactMe.query.all()
    menus=Portfoliomenu.query.all()
    links=Portfolio.query.all()
    tests=Testi.query.all()
    stars=Testimioanalstar.query.all()
    blogs=Blog.query.all()
    posts=AboutImg.query.all()
    ends=End.query.all()
    return loginCheck(render_template('admin/index.html', logos=logos,icons=icons,profiles=profiles,profiletxts=profiletxts,aboutheads=aboutheads, skills=skills,menus=menus, hobbys=hobbys, socials=socials,endicons=endicons,
    links=links,posts=posts,tests=tests,stars=stars, infos=infos, offers=offers,edus=edus,blogs=blogs,ends=ends))



# logo img
@app.route('/admin/logo', methods=['GET','POST']) 
def logoimg():
   logos=NavbarImg.query.all()
   if request.method=='POST':
      file=request.files['logo_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      logo=NavbarImg(
       logo_img=filename

      )     
      db.session.add(logo)
      db.session.commit()
      return redirect('/admin/logo')
   return loginCheck (render_template('admin/logo.html',logos=logos))

# delete
@app.route("/admin/logodelete/<id>")
def logodelete(id):
   logo=NavbarImg.query.get(id)
   db.session.delete(logo)
   db.session.commit()
   return redirect('/admin/logo')


# update
@app.route("/admin/logoupdate/<id>" , methods=['GET','POST']) 
def logoupdate(id):
   logo=NavbarImg.query.get(id)
   if request.method=='POST':
      file=request.files['logo_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      logo.logo_img=filename
      db.session.commit()
      return redirect('/admin/logo')
   return loginCheck (render_template('admin/logoupdate.html',logo=logo))

#  end


# navbar icon
@app.route('/admin/navbaricon', methods=['GET','POST']) 
def navbaricon():
   icons=NavbarIcon.query.all()
   if request.method=='POST':
      icon=NavbarIcon(
      nav_icon_name=request.form['nav_icon_name'],
      nav_icon=request.form['nav_icon'],
      nav_icon_url=request.form['nav_icon_url']
      )     
      db.session.add(icon)
      db.session.commit()
      return redirect('/admin/navbaricon')
   return  loginCheck( render_template('admin/navbaricon.html',icons=icons))
   
   # update
@app.route("/admin/navbariconupdate/<id>" , methods=['GET','POST'])  
def navbariconupdate(id):
   icon=NavbarIcon.query.get(id)
   if request.method=='POST':
      icon.nav_icon_name=request.form['nav_icon_name']
      icon.nav_icon=request.form['nav_icon']
      icon.nav_icon_url=request.form['nav_icon_url']

      db.session.commit()
      return redirect('/admin/navbaricon')
   return loginCheck (render_template('admin/navbariconupdate.html',icon=icon))

@app.route("/admin/navbaricondelete/<id>")
def navbaricondelete(id):
   icon=NavbarIcon.query.get(id)
   db.session.delete(icon)
   db.session.commit()
   return redirect('/admin/navbaricon')

# profile img
@app.route('/admin/profileimg', methods=['GET','POST']) 
def profileimg():
   profiles=ProfileImg.query.all()
   if request.method=='POST':
      file=request.files['profile_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      profile=ProfileImg(
       profile_img=filename

      )     
      db.session.add(profile)
      db.session.commit()
      return redirect('/admin/profileimg')
   return loginCheck (render_template('admin/profileimg.html',profiles=profiles))

# delete
@app.route("/admin/profileimgdelete/<id>")
def profileimgdelete(id):
   profile=ProfileImg.query.get(id)
   db.session.delete(profile)
   db.session.commit()
   return redirect('/admin/profileimg')


# update
@app.route("/admin/profileimgupdate/<id>" , methods=['GET','POST']) 
def profileimgupdate(id):
   profile=ProfileImg.query.get(id)
   if request.method=='POST':
      file=request.files['profile_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      profile.profile_img=filename
      db.session.commit()
      return redirect('/admin/profileimg')
   return loginCheck (render_template('admin/profileimgupdate.html',profile=profile))


# 

# profile txt
@app.route('/admin/profiletxt', methods=['GET','POST']) 
def profiletxt():
   profiletxts=ProfileTxt.query.all()
   if request.method=='POST':
      profiletxt=ProfileTxt(
      profile_txt=request.form['profile_txt']
      )     
      db.session.add(profiletxt)
      db.session.commit()
      return redirect('/admin/profiletxt')
   return  loginCheck( render_template('admin/profiletxt.html',profiletxts=profiletxts))
   
   # update
@app.route("/admin/profiletxtupdate/<id>" , methods=['GET','POST'])  
def profiletxtupdate(id):
   profiletxt=ProfileTxt.query.get(id)
   if request.method=='POST':
      profiletxt.profile_txt=request.form['profile_txt']
      db.session.commit()
      return redirect('/admin/profiletxt')
   return loginCheck (render_template('admin/profiletxtupdate.html',profiletxt=profiletxt))

@app.route("/admin/profiletxtdelete/<id>")
def profiletxtdelete(id):
   profiletxt=ProfileTxt.query.get(id)
   db.session.delete(profiletxt)
   db.session.commit()
   return redirect('/admin/profiletxt')

# 


# about img
@app.route('/admin/aboutimg', methods=['GET','POST']) 
def aboutimg():
   posts=AboutImg.query.all()
   if request.method=='POST':
      file=request.files['about_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      post=AboutImg(
       about_img=filename

      )     
      db.session.add(post)
      db.session.commit()
      return redirect('/admin/aboutimg')
   return loginCheck (render_template('admin/aboutimg.html',posts=posts))

# delete
@app.route("/admin/aboutimgdelete/<id>")
def Aboutimgdelete(id):
   post=AboutImg.query.get(id)
   db.session.delete(post)
   db.session.commit()
   return redirect('/admin/aboutimg')


# update
@app.route("/admin/aboutimgupdate/<id>" , methods=['GET','POST']) 
def Aboutimgupdate(id):
   post=AboutImg.query.get(id)
   if request.method=='POST':
      file=request.files['about_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      post.about_img=filename
      db.session.commit()
      return redirect('/admin/aboutimg')
   return loginCheck (render_template('admin/aboutimgupdate.html',post=post))

#  end

# about heading
@app.route('/admin/abouthead', methods=['GET','POST']) 
def abouthead():
   aboutheads=AboutHeading.query.all()
   if request.method=='POST':
      abouthead=AboutHeading(
      about_heading=request.form['about_heading']
      )     
      db.session.add(abouthead)
      db.session.commit()
      return redirect('/admin/abouthead')
   return  loginCheck( render_template('admin/abouthead.html',aboutheads=aboutheads))
   
   # update
@app.route("/admin/aboutheadupdate/<id>" , methods=['GET','POST'])  
def aboutheadupdate(id):
   abouthead=AboutHeading.query.get(id)
   if request.method=='POST':
      abouthead.about_heading=request.form['about_heading']
      db.session.commit()
      return redirect('/admin/abouthead')
   return loginCheck (render_template('admin/aboutheadupdate.html',abouthead=abouthead))

@app.route("/admin/aboutheaddelete/<id>")
def aboutheaddelete(id):
   abouthead=AboutHeading.query.get(id)
   db.session.delete(abouthead)
   db.session.commit()
   return redirect('/admin/abouthead')

# 

@app.route('/admin/aboutskill', methods=['GET','POST']) 
def aboutskill():
   skills=Skill.query.all()
   if request.method=='POST':
      skill=Skill(
      skill_name=request.form['skill_name']
      )     
      db.session.add(skill)
      db.session.commit()
      return redirect('/admin/aboutskill')
   return  loginCheck( render_template('admin/aboutskill.html',skills=skills))
   
   # update
@app.route("/admin/aboutskillupdate/<id>" , methods=['GET','POST'])  
def aboutskillupdate(id):
   skill=Skill.query.get(id)
   if request.method=='POST':
      skill.skill_name=request.form['skill_name']
      db.session.commit()
      return redirect('/admin/aboutskill')
   return loginCheck (render_template('admin/aboutskillupdate.html',skill=skill))

@app.route("/admin/aboutskilldelete/<id>")
def aboutskilldelete(id):
   skill=Skill.query.get(id)
   db.session.delete(skill)
   db.session.commit()
   return redirect('/admin/aboutskill')

# hobby
@app.route('/admin/hobby', methods=['GET','POST']) 
def hobby():
   hobbys=Hobby.query.all()
   if request.method=='POST':
      hobby=Hobby(
      hobby_icon_name=request.form['hobby_icon_name'],
      hobby_icon=request.form['hobby_icon'],
      hobby_desc=request.form['hobby_desc']
      )     
      db.session.add(hobby)
      db.session.commit()
      return redirect('/admin/hobby')
   return  loginCheck( render_template('admin/hobby.html',hobbys=hobbys))
   
   # update
@app.route("/admin/hobbyupdate/<id>" , methods=['GET','POST'])  
def hobbyupdate(id):
   hobby=Hobby.query.get(id)
   if request.method=='POST':
      hobby.hobby_icon_name=request.form['hobby_icon_name']
      hobby.hobby_icon=request.form['hobby_icon']
      hobby.hobby_desc=request.form['hobby_desc']

      db.session.commit()
      return redirect('/admin/hobby')
   return loginCheck (render_template('admin/hobbyupdate.html',hobby=hobby))

@app.route("/admin/hobbydelete/<id>")
def hobbydelete(id):
   hobby=Hobby.query.get(id)
   db.session.delete(hobby)
   db.session.commit()
   return redirect('/admin/hobby')
# 

# Counter
@app.route('/admin/count', methods=['GET','POST']) 
def count():
   infos=Counter.query.all()
   if request.method=='POST':
      info=Counter(
      counter_icon_name=request.form['counter_icon_name'],
      counter_icon=request.form['counter_icon'],
      counter_count=request.form['counter_count'],
      counter_txt=request.form['counter_txt']
      )     
      db.session.add(info)
      db.session.commit()
      return redirect('/admin/count')
   return  loginCheck( render_template('admin/count.html',infos=infos))
   
   # update
@app.route("/admin/countupdate/<id>" , methods=['GET','POST'])  
def countupdate(id):
   info=Counter.query.get(id)
   if request.method=='POST':
      info.counter_icon_name=request.form['counter_icon_name']
      info.counter_icon=request.form['counter_icon']
      info.counter_count=request.form['counter_count']
      info.counter_txt=request.form['counter_txt']

      db.session.commit()
      return redirect('/admin/count')
   return loginCheck (render_template('admin/countupdate.html',info=info))

@app.route("/admin/countdelete/<id>")
def countdelete(id):
   info=Counter.query.get(id)
   db.session.delete(info)
   db.session.commit()
   return redirect('/admin/count')

# 

# offer
@app.route('/admin/offer', methods=['GET','POST']) 
def offer():
   offers=Offer.query.all()
   if request.method=='POST':
      offer=Offer(
      offer_icon_name=request.form['offer_icon_name'],
      offer_icon=request.form['offer_icon'],
      offer_back_icon=request.form['offer_back_icon'],
      offer_heading=request.form['offer_heading'],
      offer_desc=request.form['offer_desc']

      )     
      db.session.add(offer)
      db.session.commit()
      return redirect('/admin/offer')
   return  loginCheck( render_template('admin/offer.html',offers=offers))
   
   # update
@app.route("/admin/offerupdate/<id>" , methods=['GET','POST'])  
def offerupdate(id):
   offer=Offer.query.get(id)
   if request.method=='POST':
      offer.offer_icon_name=request.form['offer_icon_name']
      offer.offer_icon=request.form['offer_icon']
      offer.offer_back_icon=request.form['offer_back_icon']
      offer.offer_heading=request.form['offer_heading']
      offer.offer_desc=request.form['offer_desc']
      db.session.commit()
      return redirect('/admin/offer')
   return loginCheck (render_template('admin/offerupdate.html',offer=offer))

@app.route("/admin/offerdelete/<id>")
def offerdelete(id):
   offer=Offer.query.get(id)
   db.session.delete(offer)
   db.session.commit()
   return redirect('/admin/offer')


# 


# education 

@app.route('/admin/edu', methods=['GET','POST']) 
def edu():
   edus=Education.query.all()
   if request.method=='POST':
      edu=Education(
      start_date=request.form['start_date'],
      end_date=request.form['end_date'],
      edu_heading=request.form['edu_heading'],
      edu_desc=request.form['edu_desc']
      )     
      db.session.add(edu)
      db.session.commit()
      return redirect('/admin/edu')
   return  loginCheck( render_template('admin/edu.html',edus=edus))

@app.route("/admin/eduupdate/<id>" , methods=['GET','POST'])  
def eduupdate(id):
   edu=Education.query.get(id)
   if request.method=='POST':
      edu.start_date=request.form['start_date']
      edu.end_date=request.form['end_date']
      edu.edu_heading=request.form['edu_heading']
      edu.edu_desc=request.form['edu_desc']
      db.session.commit()
      return redirect('/admin/edu')
   return loginCheck (render_template('admin/eduupdate.html',edu=edu))

@app.route("/admin/edudelete/<id>")
def edudelete(id):
   edu=Education.query.get(id)
   db.session.delete(edu)
   db.session.commit()
   return redirect('/admin/edu')

# 


# portfolio menu
@app.route('/admin/portmenu', methods=['GET','POST']) 
def portmenu():
   menus=Portfoliomenu.query.all()
   if request.method=='POST':
      menu=Portfoliomenu(
      portfolio_menu_name=request.form['portfolio_menu_name']
      )     
      db.session.add(menu)
      db.session.commit()
      return redirect('/admin/portmenu')
   return  loginCheck( render_template('admin/portmenu.html',menus=menus))
   
   # update
@app.route("/admin/portmenuupdate/<id>" , methods=['GET','POST'])  
def portheadupdate(id):
   menu=Portfoliomenu.query.get(id)
   if request.method=='POST':
      menu.portfolio_menu_name=request.form['portfolio_menu_name']
      db.session.commit()
      return redirect('/admin/portmenu')
   return loginCheck (render_template('admin/portmenuupdate.html',menu=menu))

@app.route("/admin/portmenudelete/<id>")
def portheaddelete(id):
   menu=Portfoliomenu.query.get(id)
   db.session.delete(menu)
   db.session.commit()
   return redirect('/admin/portmenu')

# 

# Portfolio
@app.route('/admin/portfolio', methods=['GET','POST']) 
def portfolio():
   links=Portfolio.query.all()
   if request.method=='POST':
      file=request.files['portfolio_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      link=Portfolio(
         portfolio_img_link=request.form['portfolio_img_link'],
         portfolio_img_head=request.form['portfolio_img_head'],
         portfolio_img_desc=request.form['portfolio_img_desc'],
         portfolio_img=filename

      )     
      db.session.add(link)
      db.session.commit()
      return redirect('/admin/portfolio')
   return loginCheck( render_template('admin/portfolio.html',links=links))

# delete
@app.route("/admin/portfoliodelete/<id>")
def porfoliodelete(id):
   link=Portfolio.query.get(id)
   db.session.delete(link)
   db.session.commit()
   return redirect('/admin/portfolio')


# update
@app.route("/admin/portfolioupdate/<id>" , methods=['GET','POST']) 
def portfolioupdate(id):
   link=Portfolio.query.get(id)
   if request.method=='POST':
      file=request.files['portfolio_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      link.portfolio_img_link=request.form['portfolio_img_link']
      link.portfolio_img_head=request.form['portfolio_img_head']
      link.portfolio_img_desc=request.form['portfolio_img_desc']
      link.portfolio_img=filename
      db.session.commit()
      return redirect('/admin/portfolio')
   return loginCheck (render_template('admin/portfolioupdate.html',link=link))

# 


# testimional heading


@app.route('/admin/star', methods=['GET','POST']) 
def star():
   stars=Testimioanalstar.query.all()
   if request.method=='POST':
      file=request.files['testi_slider_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      star=Testimioanalstar(
      testi_heading=request.form['testi_heading'],
      testi_desc=request.form['testi_desc'],
      testi_slider_head=request.form['testi_slider_head'],
      testi_slider_desc=request.form['testi_slider_desc'],
       testi_slider_img=filename    
      )     
      db.session.add(star)
      db.session.commit()
      return redirect('/admin/star')
   return  loginCheck( render_template('admin/star.html',stars=stars))
   
   # update
@app.route("/admin/starupdate/<id>" , methods=['GET','POST'])  
def starupdate(id):
   star=Testimioanalstar.query.get(id)
   if request.method=='POST':
      file=request.files['testi_slider_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      star.testi_heading=request.form['testi_heading']
      star.testi_desc=request.form['testi_desc']
      star.testi_slider_head=request.form['testi_slider_head']
      star.testi_slider_desc=request.form['testi_slider_desc']
      star.testi_desc=request.form['testi_desc']
      star.testi_slider_img=filename
      db.session.commit()
      return redirect('/admin/star')
   return loginCheck (render_template('admin/starupdate.html',star=star))

@app.route("/admin/stardelete/<id>")
def stardelete(id):
   star=Testimioanalstar.query.get(id)
   db.session.delete(star)
   db.session.commit()
   return redirect('/admin/star')

# 


# testimioanal img
@app.route('/admin/testiimg', methods=['GET','POST']) 
def testiimg():
   tests=Testi.query.all()
   if request.method=='POST':
      file=request.files['testimional_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      test=Testi(
       testimional_img=filename

      )     
      db.session.add(test)
      db.session.commit()
      return redirect('/admin/testiimg')
   return loginCheck (render_template('admin/testiimg.html',tests=tests))

# delete
@app.route("/admin/testiimgdelete/<id>")
def Testidelete(id):
   test=Testi.query.get(id)
   db.session.delete(test)
   db.session.commit()
   return redirect('/admin/testiimg')


# update
@app.route("/admin/testiimgupdate/<id>" , methods=['GET','POST']) 
def Testiupdate(id):
   test=Testi.query.get(id)
   if request.method=='POST':
      file=request.files['testimional_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      test.testimional_img=filename
      db.session.commit()
      return redirect('/admin/testiimg')
   return loginCheck (render_template('admin/testiimgupdate.html',test=test))


#Blog
@app.route('/admin/blog', methods=['GET','POST']) 
def blog():
   blogs=Blog.query.all()
   if request.method=='POST':
      file=request.files['blog_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      blog=Blog(
         blog_img_url=request.form['blog_img_url'],
         blog_desc=request.form['blog_desc'],
         blog_read_more_url=request.form['blog_read_more_url'],
         blog_date =request.form['blog_date'],
         blog_img=filename

      )     
      db.session.add(blog)
      db.session.commit()
      return redirect('/admin/blog')
   return loginCheck( render_template('admin/blog.html',blogs=blogs))

# delete
@app.route("/admin/blogdelete/<id>")
def blogdelete(id):
   blog=Blog.query.get(id)
   db.session.delete(blog)
   db.session.commit()
   return redirect('/admin/blog')


# update
@app.route("/admin/blogupdate/<id>" , methods=['GET','POST']) 
def blogupdate(id):
   blog=Blog.query.get(id)
   if request.method=='POST':
      file=request.files['blog_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      blog.blog_img_url=request.form['blog_img_url']
      blog.blog_desc=request.form['blog_desc']
      blog.blog_read_more_url=request.form['blog_read_more_url']
      blog.blog_date=request.form['blog_date']
      blog.blog_img=filename
      db.session.commit()
      return redirect('/admin/blog')
   return loginCheck (render_template('admin/blogupdate.html',blog=blog))

# 

# ContactMe

@app.route('/admin/icon', methods=['GET','POST']) 
def icon():
   endicons=ContactMe.query.all()
   if request.method=='POST':
      endicon=ContactMe(
      ct_icon_name=request.form['ct_icon_name'],
      ct_icon=request.form['ct_icon'],
      ct_heading=request.form['ct_heading'],
      ct_desc=request.form['ct_desc'],
      ct_link=request.form['ct_link'],
      ct_txt=request.form['ct_txt']
    
      )     
      db.session.add(endicon)
      db.session.commit()
      return redirect('/admin/icon')
   return loginCheck(render_template('admin/icon.html',endicons=endicons))
   
   # update
@app.route("/admin/iconupdate/<id>" , methods=['GET','POST'])  
def iconupdate(id):
   endicon=ContactMe.query.get(id)
   if request.method=='POST':
      endicon.ct_icon_name=request.form['ct_icon_name']
      endicon.ct_icon=request.form['ct_icon']
      endicon.ct_heading=request.form['ct_heading']
      endicon.ct_desc=request.form['ct_desc']
      endicon.ct_link=request.form['ct_link']
      endicon.ct_txt=request.form['ct_txt']


      db.session.commit()
      return redirect('/admin/icon')
   return loginCheck( render_template('admin/iconupdate.html',endicon=endicon))

@app.route("/admin/icondelete/<id>")
def icondelete(id):
   endicon=ContactMe.query.get(id)
   db.session.delete(endicon)
   db.session.commit()
   return redirect('/admin/icon')
# 

# End logo
@app.route('/admin/end', methods=['GET','POST']) 
def endlogo():
   ends=End.query.all()
   if request.method=='POST':
      file=request.files['end_logo_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      end=End(
      end_logo_desc=request.form['end_logo_desc'],  
       end_logo_img=filename

      )     
      db.session.add(end)
      db.session.commit()
      return redirect('/admin/end')
   return loginCheck (render_template('admin/end.html',ends=ends))

# delete
@app.route("/admin/enddelete/<id>")
def enddelete(id):
   end=End.query.get(id)
   db.session.delete(end)
   db.session.commit()
   return redirect('/admin/end')


# update
@app.route("/admin/endupdate/<id>" , methods=['GET','POST']) 
def endupdate(id):
   end=End.query.get(id)
   if request.method=='POST':
      file=request.files['end_logo_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      end.end_logo_desc=request.form['end_logo_desc']
      end.end_logo_img=filename

      db.session.commit()
      return redirect('/admin/end')
   return loginCheck (render_template('admin/endupdate.html',end=end))


# 


# Social Icon
@app.route('/admin/social', methods=['GET','POST']) 
def social():
   socials=SocialIcon.query.all()
   if request.method=='POST':
      social=SocialIcon(
      social_icon_name=request.form['social_icon_name'],
      social_icon=request.form['social_icon'],
      social_icon_url=request.form['social_icon_url']
      )     
      db.session.add(social)
      db.session.commit()
      return redirect('/admin/social')
   return loginCheck( render_template('admin/social.html',socials=socials))
   
   # update
@app.route("/admin/socialupdate/<id>" , methods=['GET','POST'])  
def socialupdate(id):
   social=SocialIcon.query.get(id)
   if request.method=='POST':
      social.social_icon_name=request.form['social_icon_name']
      social.social_icon=request.form['social_icon']
      social.social_icon_url=request.form['social_icon_url']

      db.session.commit()
      return redirect('/admin/social')
   return loginCheck (render_template('admin/socialupdate.html',social=social))

@app.route("/admin/socialdelete/<id>")
def socialdelete(id):
   social=SocialIcon.query.get(id)
   db.session.delete(social)
   db.session.commit()
   return redirect('/admin/social')

