# from flask import Flask, render_template, url_for, request, redirect
# from flask_sqlalchemy import SQLAlchemy
import requests

# _DEBUG = True

_YELP_URL = 'https://api.yelp.com/v3/categories/alias'
_GEOCODING_URL = 'https://nominatim.openstreetmap.org/search?format=json&q='

def send_request(text: str):
    """ Sends a GET request to the Yelp Fusion API
        to access restaurants that are within a 20 mile radius
        from the user's current location"""









# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)

# class YelpList(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)

#     def __reqr__(self):
#         return '<Item %r>' % self.id



# @app.route('/')
# def index():  # put application's code here
#     return render_template('index.html')

# @app.route('/', methods=['POST'])
# def post_search():
#     if request.method == 'POST':
#         text = request.form['search_query']
#         if text:
#             # yelp_return = requests.get()
#             return render_template('post_search.html', result1 = text)
#     return render_template('index.html')


# if __name__ == '__main__':
#     app.run(host = 'localhost', port = 8000, debug = True)
