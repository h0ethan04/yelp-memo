# Yelp Memo

Yelp Memo is a web application designed to allow authenticated
users to save visited locations and add notes, such as orders,
to said locations.

# Usage

If you would like to see a preview of my website, please send me
an email at hoea2 *at* uci *dot* edu. Begin the subject line with "Yelp-Memo"
and include what you plan to use the preview for.

If you would like to host your own version of this website:

1. clone this repo and install dependencies according to `requirements.txt`
2. create a MySQL database on a server that you have access to
    1. for testing purposes, I suggest downloading [MySQL Community Edition](https://dev.mysql.com/downloads/ "MySQL CE")
    2. alternatively, you can host a MySQL database on Azure or AWS and connect that database
3. create a Yelp developer account to gain access to [Yelp Fusion](https://fusion.yelp.com/ "Yelp Fusion API")
4. navigate to the website folder in your repo, and add a file named `config.py`
5. within the `config.py` file, you will define 8 variables:
    - APP_KEY: secret key (I suggest you use secrets.token_hex(16) or 
    another random hex generator to create one)
    - YELP_KEY: key from the Yelp developer account
    - _DEBUG: set to False to access the Yelp API upon query;
    set to True and pair with a `sample.json` file using [this format](#sample-data "Goto sample data") in order to use your app without querying the Yelp Fusion API
    - MYSQL_HOST: MySQL host; use `localhost` if hosting a local database
    - MYSQL_PORT: default MySQL port is 3306
    - MYSQL_USER: MySQL username used to access the database
    - MYSQL_PASSWORD: MySQL password used to access the database
    - MYSQL_DB: the name of your MySQL database
6. run `app.py`

# Sample data
```json
{
    "businesses": [
      {
        "id": "vKAO9HNM4n7kGRQH18wIzA",
        "alias": "rose-tea-lounge-elk-grove-elk-grove",
        "name": "Rose Tea Lounge - Elk Grove",
        "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/BUxHJj79lypELpxR39g0AA/o.jpg",
        "is_closed": false,
        "url": "https://www.yelp.com/biz/rose-tea-lounge-elk-grove-elk-grove?adjust_creative=V7Cfj6d_UZ6KTTge9o5Q-g&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=V7Cfj6d_UZ6KTTge9o5Q-g",
        "review_count": 511,
        "categories": [
          {
            "alias": "bubbletea",
            "title": "Bubble Tea"
          },
          {
            "alias": "coffee",
            "title": "Coffee & Tea"
          }
        ],
        "rating": 4,
        "coordinates": {
          "latitude": 38.424965,
          "longitude": -121.392431
        },
        "transactions": [],
        "price": "$$",
        "location": {
          "address1": "9160 E Stockton Blvd",
          "address2": "Ste 120",
          "address3": null,
          "city": "Elk Grove",
          "zip_code": "95624",
          "country": "US",
          "state": "CA",
          "display_address": [
            "9160 E Stockton Blvd",
            "Ste 120",
            "Elk Grove, CA 95624"
          ]
        },
        "phone": "+19166673748",
        "display_phone": "(916) 667-3748",
        "distance": 1705.8165348965344
      }
    ],
    "total": 65,
    "region": {
      "center": {
        "longitude": -121.38862609863281,
        "latitude": 38.4099751396218
      }
    }
  }
```