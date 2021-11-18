from enum import unique
from app import db


class NavbarImg(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    logo_img=db.Column(db.String(50))

 
class NavbarIcon(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nav_icon_name=db.Column(db.String(50))
    nav_icon=db.Column(db.String(50))
    nav_icon_url=db.Column(db.String(50))

 
class ProfileImg(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    profile_img=db.Column(db.String(50))

class ProfileTxt(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    profile_txt=db.Column(db.String(50))

class AboutImg(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    about_img=db.Column(db.String(50))

class AboutHeading(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    about_heading=db.Column(db.String(50))


class Skill(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    skill_name=db.Column(db.String(50))


class Hobby(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    hobby_icon_name=db.Column(db.String(50))
    hobby_icon=db.Column(db.String(50))
    hobby_desc=db.Column(db.String(50))

class Counter(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    counter_icon_name=db.Column(db.String(50))
    counter_icon=db.Column(db.String(50))
    counter_count=db.Column(db.String(50))
    counter_txt=db.Column(db.String(50))	

class Offer(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    offer_icon_name=db.Column(db.String(50))
    offer_icon=db.Column(db.String(50))
    offer_back_icon=db.Column(db.String(50))
    offer_heading=db.Column(db.String(50))
    offer_desc=db.Column(db.String(50))


class Education(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    start_date=db.Column(db.String(50))
    end_date=db.Column(db.String(50))
    edu_heading=db.Column(db.String(50))
    edu_desc=db.Column(db.String(50))


class Portfoliomenu (db.Model):
    id=db.Column(db.Integer,primary_key=True)
    portfolio_menu_name=db.Column(db.String(50))

class Portfolio(db.Model):
 id=db.Column(db.Integer,primary_key=True)
 portfolio_img=db.Column(db.String(50))
 portfolio_img_head=db.Column(db.String(50)) 
 portfolio_img_desc=db.Column(db.String(50)) 
 portfolio_img_link=db.Column(db.String(50)) 

class Testimioanalstar (db.Model):
    id=db.Column(db.Integer,primary_key=True)
    testi_heading=db.Column(db.String(50))
    testi_desc=db.Column(db.String(50))
    testi_slider_img=db.Column(db.String(50))
    testi_slider_head=db.Column(db.String(50))
    testi_slider_desc=db.Column(db.String(50))
    


class Testi (db.Model):
	id=db.Column(db.Integer,primary_key=True)
	testimional_img=db.Column(db.String(50))


	
class Blog (db.Model):
	id=db.Column(db.Integer,primary_key=True)
	blog_img=db.Column(db.String(50))
	blog_img_url=db.Column(db.String(50))
	blog_desc=db.Column(db.String(50))
	blog_read_more_url=db.Column(db.String(50))
	blog_date=db.Column(db.String(50))

class ContactMe(db.Model):
 id=db.Column(db.Integer,primary_key=True)
 ct_icon_name=db.Column(db.String(50))
 ct_icon=db.Column(db.String(50))
 ct_heading=db.Column(db.String(50))
 ct_desc=db.Column(db.String(50)) 
 ct_link=db.Column(db.String(50)) 
 ct_txt=db.Column(db.String(50)) 



class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.String(50))
    user_email=db.Column(db.String(50))
    user_message=db.Column(db.Text)
    user_subject=db.Column(db.String(50))


class End(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	end_logo_img=db.Column(db.String(50))
	end_logo_desc=db.Column(db.String(50))

class SocialIcon(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	social_icon_name=db.Column(db.String(50))
	social_icon=db.Column(db.String(50))
	social_icon_url=db.Column(db.String(50))	
	