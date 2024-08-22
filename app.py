from flask import Flask, render_template
# from .database import db
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  " mysql://root:azhar%40123@localhost/Flask_api" #
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sno = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Todo {self.id}: {self.title}"
    

@app.route('/')
def hello():
    todo3 = Todo(title='firt Todo', desc='start inverting in Stock market')
    db.session.add(todo3)
    db.session.commit()

    return render_template('index.html')



@app.route('/shop')
def products():
    # alltodo = Todo.query.all()
    return 'this is the Product page'


app.run(debug=True, port=6000)
