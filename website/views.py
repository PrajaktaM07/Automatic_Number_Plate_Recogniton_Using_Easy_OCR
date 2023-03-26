from flask import Blueprint, render_template, request, flash, jsonify
from .models import Car
from . import db
import os
import alternate
# import json
from pprint import pprint

views = Blueprint('views', __name__)

uploads_dir = "uploads"

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST': 
        # photo = request.form.get('photo-upload')#Gets the note from the HTML 
        file1 = request.files.listvalues
        photo = request.files['photo']
        print(photo)
        photo.save(os.path.join(uploads_dir, photo.filename))
        saved_path = os.path.join(uploads_dir, photo.filename)
        print(saved_path)
        car_details = alternate.read_text(filename=saved_path)
        pprint(car_details)

        return render_template("results.html", details=car_details)
        # print(files)
        # print(photo)
        
        # if len(note) < 1:
        #     flash('Note is too short!', category='error') 
        # else:
        #     new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
        #     db.session.add(new_note) #adding the note to the database 
        #     db.session.commit()
        #     flash('Note added!', category='success')

    return render_template("home.html")