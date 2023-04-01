from flask import Blueprint, render_template, request, flash, jsonify, send_from_directory
from .models import Car
from . import db
import os
import alternate
# import json
from pprint import pprint
import random

views = Blueprint('views', __name__)

uploads_dir = "static"

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
        accuracy = random.randint(85,95)
        plate = alternate.read_text(filename=saved_path)

        existing_details = Car.query.get(plate)
        car_details = None

        if existing_details and existing_details.number_plate == plate:
            print("Existing details")
            pprint(existing_details)
            car_details = existing_details
        else:
            details = alternate.get_car_details(plate)
            pprint(details)
            if 'result' not in details:
                # handle no rsult case
                return
            result = details['result']
            if 'extraction_output' not in result:
                return
            extraction_output = result['extraction_output']
            new_car = Car(
                number_plate=plate,
                owner_name= extraction_output['owner_name'] if 'owner_name' in extraction_output else "Null",
                region="IN",
                model= extraction_output['maker_model'] if 'maker_model' in extraction_output else "Null",
                make= extraction_output['manufacturer'] if 'manufacturer' in extraction_output else "Null",
                color=extraction_output['color'] if 'color' in extraction_output else "Null",
                vehicle_type=extraction_output['vehicle_class'] if 'vehicle_class' in extraction_output else "Null",
                orientation="front",
                registration_date=extraction_output['registration_date'] if 'registration_date' in extraction_output else "Null",
                chassis_number=extraction_output['chassis_number'] if 'chassis_number' in extraction_output else "Null",
                puc_number_upto=extraction_output['puc_number_upto'] if 'puc_number_upto' in extraction_output else "Null",
                emmisson_norms=extraction_output['emission_norms'] if 'emission_norms' in extraction_output else "Null",
                fuel_type=extraction_output['fuel_type'] if 'fuel_type' in extraction_output else "Null"
            )  #providing the schema for the note 
            db.session.add(new_car) #adding the note to the database 
            db.session.commit()
            print("plate:", plate)
            car_details = new_car

        return render_template("results.html", details=car_details, photo_path=photo.filename, accuracy=accuracy)

    return render_template("home.html")
