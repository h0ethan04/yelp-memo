from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
import json
from .models import Note
from . import db

from .yelp import send_request, _DEBUG

views = Blueprint('views', __name__)

@views.route('/', methods=['POST', 'GET'])
@login_required
def home():
    """ Handles requests made when on the search screen"""

    if request.method == 'POST':
        search_query = request.form.get('search_query')
        location_query = request.form.get('location_query')

        if not search_query:
            flash('Please enter a search term', category='error')
            return render_template('index.html', user=current_user, data=None)
        elif not location_query:
            flash('Please enter a valid location', category='error')
            return render_template('index.html', user=current_user, data=None)
        else:
            if _DEBUG:
                # print(send_request('boba', 'irvine', 5000)['businesses'][0])
                return render_template('index.html', user=current_user, data=send_request('boba', 'irvine', 5000)['businesses'])
            else:
                return render_template('index.html', user=current_user, data=send_request(search_query, location_query, 20000)['businesses'])
    else:
        return render_template('index.html', user=current_user, data=None)




@views.route('/saved', methods=['POST', 'GET'])
def notes():
    """ Handles the page where saved locations and notes about those locations
        are accessible"""
    if request.method == 'POST':
        pass
    return render_template('saved.html', user=current_user)

@views.route('/save-note', methods = ['POST'])
def save_note():
    note = json.loads(request.data)
    if not Note.query.filter_by(business_id=note['business_id']).first():
        name = note['name']
        img = note['img']
        address = note['address']
        phone = note['phone']
        url = note['url']
        rating = round(note['rating'], 2)
        business_id = note['business_id']
        new_note = Note(name=name, img=img, address=address, phone=phone, url=url, rating=rating, business_id=business_id, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
        # flash('Saved to your collection!', category='success')

    return jsonify({})
    

@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash('Location deleted', category='success')

    return jsonify({})