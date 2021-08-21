from flask import Flask,render_template,request
from werkzeug.utils import redirect

Books = []

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create_book', methods = ['GET', 'POST'])
def create_book():
    if request.method == 'POST':
        Name = request.form['Name']
        Author = request.form['Author']
        Year = request.form['Year']
        Number = request.form['Number']
        Summary = request.form['Summary']
        Book = {
            'id':Books.__len__(),
            'Name': Name,
            'Author': Author,
            'Year': Year,
            'Number': Number,
            'Summary': Summary
        }
        Books.append(Book)
        
        
    return render_template('create.html')



@app.route('/show')
def show():
    return render_template('show.html', Books = Books)

@app.route('/single/<id>')
def single(id):
    id=int(id)
    book={}

    for i in Books:
       if id==i['id']:
           book=i
    return render_template('single.html',book=book) 
    

@app.route('/admin')
def admin():
    return render_template('admin.html', Books = Books)


@app.route('/delete/<int:id>')
def delete(id):
    for book in Books:
        if id==book['id']:
           Books.remove(book)
    return redirect('/admin')


@app.route('/update/<int:id>',methods=['POST','GET'])
def update(id):
    data={}
    for book in Books:
        if id==book['id']:
            data=book
            if request.method=='POST':
                Name=request.form['Name']
                Author=request.form['Author']
                Year=request.form['Year']
                Number=request.form['Number']
                Summary=request.form['Summary']
                Books.remove(book)
                data={
                    'id':book['id'],
                    'Name':Name,
                    'Author':Author,
                    'Year':Year,
                    'Number':Number,
                    'Summary':Summary
                }
                Books.append(data)
                return redirect('/admin')
    return render_template('update.html',data=data)



if __name__=='__main__':
    app.run(debug=True)