from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'
db = SQLAlchemy(app)

class Newss(db.Model):
    news_id = db.Column(db.Integer, primary_key=True)
    news_title = db.Column(db.String(120))
    news_desc = db.Column(db.String(500))

@app.route('/')
def index():
    return render_template('index.html')



@app.route("/create_news", methods=["GET","POST"])
def create_news():
    News=Newss.query.all()
    if request.method=="POST":
       
        Title = request.form['Title']
        Desc = request.form['Desc']
        
        singleNews = Newss(
            news_title=Title,
            news_desc=Desc
        )
        db.session.add(singleNews)
        db.session.commit()
        return redirect("/create_news")
    return render_template("create.html")

@app.route("/admin")
def admin():
    News=Newss.query.all()
    return render_template("admin.html",News=News)



@app.route('/show')
def show():
    News=Newss.query.all()
    return render_template('show.html', News = News)
    

@app.route('/single/<id>')
def single(id):
    News=Newss.query.all()

    news_id=int(id)
    news={}

    for i in News:
        if news_id==i['id']:
            news=i
    return render_template('single.html',news=news) 


@app.route('/delete/<id>')
def delete(id):
    News=Newss.query.all()
    news_id=int(id)
    for i in News:
        if news_id==i['id']:
           News.remove(i)
    return redirect('/admin')

db.create_all()


if __name__=="__main__":
    app.run(debug=True)