
import requests
from .config import YELP_KEY, _DEBUG
import json

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