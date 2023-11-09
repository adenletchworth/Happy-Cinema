from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import web_scraper as wc 
import language_processing as lp  

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)

class Cinema(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    genre = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(20), nullable=False)
    url = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Movie %r>' % self.id


@app.route('/', methods=['GET', 'POST'])
def index():
    movie = None
    if request.method == 'POST':
        title = request.form['title']
        url = wc.UrlPredictor(title)  
        user_movie = wc.MovieScraper(url)
 
        user_movie.find_movie_attributes() 
        movie_attributes = user_movie.movie_attributes

        if (movie_attributes == {}):
            return render_template('index.html') 
        
        movie = lp.processInput(
            user_description=movie_attributes['Description'],
            user_genre=movie_attributes['Genre']
        )

    return render_template('index.html', movie=movie)


if __name__ == "__main__":
    app.run(debug=True)
