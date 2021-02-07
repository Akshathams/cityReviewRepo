from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///worldview.db'

db = SQLAlchemy(app)

class World(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(50),nullable=False)
    review = db.Column(db.String(100),nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_city = request.form.get('city')
        new_review = request.form.get('review')
        if new_city:
            new_city_obj = World(city_name=new_city, review=new_review)
            db.session.add(new_city_obj)
            db.session.commit()
    cities = World.query.all()
    return render_template('index.html',cities=cities)
