from . import db

class Car(db.Model):
    number_plate = db.Column(db.String, primary_key=True)
    owner_name = db.Column(db.String(150))
    region = db.Column(db.String(150))
    model = db.Column(db.String(150))
    make =  db.Column(db.String(150))
    color =  db.Column(db.String(30))
    vehicle_type = db.Column(db.String(20))
    orientation = db.Column(db.String(150))
    registration_date = db.Column(db.String(150))
    chasis_number = db.Column(db.String(150))
    puc =  db.Column(db.String(10))
    emmisson_norms =  db.Column(db.String(150))
    fuel_type =  db.Column(db.String(20))