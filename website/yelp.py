
import requests
from .config import YELP_KEY
import json

_DEBUG = True
# _GEOCODING_URL = 'https://nominatim.openstreetmap.org/search?format=json&q='

_YELP_URL = 'https://api.yelp.com/v3/businesses/search?'

def send_request(text: str, location: str | tuple[float, float], radius_miles: int):
    """ Sends a GET request to the Yelp Fusion API
        to access restaurants that are within a certain radius
        from the user's current location"""
    
    radius_meters = min(40000, convert_miles_to_meters(radius_miles))
    yelp_headers = {'Authorization': f'Bearer {YELP_KEY}',
                    'accept': 'application/json'}

    payload = {#'categories': ['coffee', 'bubble tea'],
               'radius': radius_meters,
               'sort_by': 'best_match',
               'limit': '50',
               #'price': [1, 2, 3, 4],
               'term': text}

    if type(location) == tuple:
        payload['longitude'] = location[0]
        payload['latitude'] = location[1]
    else:
        payload['location'] = location


    if _DEBUG:
        with open('sample.json') as json_file:
            data = json.load(json_file)
    else:
        response = requests.get(_YELP_URL, headers=yelp_headers, params=payload)
        data = response.json()

    return data 


def convert_miles_to_meters(dist: int) -> int:
    return int(dist * 1609.34)



# if __name__ == '__main__':
#     send_request('Boba', 'Irvine', 5)





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
