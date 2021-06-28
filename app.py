from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from os import getenv


app = Flask(__name__)

app.config['SECRET_KEY'] = getenv('SKEY')
# export SKEY=[...]
# echo ${SKEY}


sowing_season = {"oregano":"from February until May.", "parsley":"from March until June.", "rosemary":"from March until May.", "sage":"from March until May.", "thyme":"from March until April; best planted from April until August."}
lifespan = {"oregano":"five to six years.", "parsley":"two years.", "rosemary":"ten years or more.", "sage":"four to five years.", "thyme":"five to six years."}
harvest_season = {"oregano":"from May until October.", "parsley":"from June until August.", "rosemary":"all year round.", "sage":"from June until November.", "thyme":"all year round."}

class Herbs(FlaskForm):
    full_name = StringField('What is your name?')
    herbs_of_interest = SelectField('Which herb would you like to grow?', choices=('None', 'Oregano', 'Parsley', 'Rosemary', 'Sage', 'Thyme'))
    herb_info = SelectField('What information do you need?', choices=('None', 'Sowing Season', 'Harvest Season', 'Lifespan'))
    submit = SubmitField('Submit Request')


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])

def submission():
    error = ""
    form = Herbs()

    
    if request.method == 'POST':
        full_name = form.full_name.data
        herbs_of_interest = form.herbs_of_interest.data
        herb_info = form.herb_info.data

        if herbs_of_interest == "Oregano" and herb_info == "Sowing Season":
            return "Hi " + str(full_name) + "! Oregano is best sown " + str(sowing_season["oregano"])
        elif herbs_of_interest == "Oregano" and herb_info == "Harvest Season":
            return "Hi " + str(full_name) + "! Oregano is best harvested " + str(harvest_season["oregano"])
        elif herbs_of_interest == "Oregano" and herb_info == "Lifespan":
            return "Hi " + str(full_name) + "! Oregano usually lives for " + str(lifespan["oregano"])

        elif herbs_of_interest == "Parsley" and herb_info == "Sowing Season":
            return "Hi " + str(full_name) + "! Parsley is best sown " + str(sowing_season["parsley"])
        elif herbs_of_interest == "Parsley" and herb_info == "Harvest Season":
            return "Hi " + str(full_name) + "! Parsley is best harvested " + str(harvest_season["parsley"])
        elif herbs_of_interest == "Parsley" and herb_info == "Lifespan":
            return "Hi " + str(full_name) + "! Parsley usually lives for " + str(lifespan["parsley"])

        elif herbs_of_interest == "Rosemary" and herb_info == "Sowing Season":
            return "Hi " + str(full_name) + "! Rosemary is best sown " + str(sowing_season["rosemary"])
        elif herbs_of_interest == "Rosemary" and herb_info == "Harvest Season":
            return "Hi " + str(full_name) + "! Rosemary is best harvested " + str(harvest_season["rosemary"])
        elif herbs_of_interest == "Rosemary" and herb_info == "Lifespan":
            return "Hi " + str(full_name) + "! Rosemary usually lives for " + str(lifespan["rosemary"])

        elif herbs_of_interest == "Sage" and herb_info == "Sowing Season":
            return "Hi " + str(full_name) + "! Sage is best sown " + str(sowing_season["sage"])
        elif herbs_of_interest == "Sage" and herb_info == "Harvest Season":
            return "Hi " + str(full_name) + "! Sage is best harvested " + str(harvest_season["sage"])
        elif herbs_of_interest == "Sage" and herb_info == "Lifespan":
            return "Hi " + str(full_name) + "! Sage usually lives for " + str(lifespan["sage"])

        elif herbs_of_interest == "Thyme" and herb_info == "Sowing Season":
            return "Hi " + str(full_name) + "! Thyme is best sown " + str(sowing_season["thyme"])
        elif herbs_of_interest == "Thyme" and herb_info == "Harvest Season":
            return "Hi " + str(full_name) + "! Thyme is best harvested " + str(harvest_season["thyme"])
        elif herbs_of_interest == "Thyme" and herb_info == "Lifespan":
            return "Hi " + str(full_name) + "! Thyme usually lives for " + str(lifespan["thyme"])
        else:
            error = "Invalid options selected, try again mate."



    return render_template('herbs.html', title='Plant Information', form=Herbs(), message=error)

if __name__ == '__main__':
     app.run(port=5000, debug=True, host='0.0.0.0') 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@34.142.112.102:3306/herb_info'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app) 

class Herbs(db.Model):
    id = db.Column('ID', db.Integer, primary_key=True)
    plant_name = db.Column('Plant Name', db.String(30), nullable=False)
    genus = db.Column('Genus', db.String(30), nullable=False)
    lifecycle = db.Column('Lifecycle', db.String(30), nullable=False)
    season_to_sow = db.Column('Season to Sow', db.String(100), nullable=False)
    season_to_harvest = db.Column('Season to Harvest', db.String(100), nullable=False)
    lifespan =  db.Column('Lifespan', db.String(100),nullable=False)
    order = db.relationship('Nursery', backref='herb')
    
class Patrons(db.Model):
    id = db.Column('ID',db.Integer, primary_key=True)
    first_name = db.Column('First Name', db.String(20), nullable=False)
    last_name = db.Column('Surname', db.String(40), nullable=False)
    email_address = db.Column('Email Address', db.String(50), nullable=False)
    order = db.relationship('Nursery', backref='patron')

class Nursery(db.Model):
    id = db.Column('Nursery ID', db.Integer, primary_key=True)
    patrons_id = db.Column('Patron Number', db.Integer,  db.ForeignKey('patrons.ID'), nullable=False)
    herbs_id = db.Column('Herb ID', db.Integer, db.ForeignKey('herbs.ID'), nullable=False)

if __name__ == '__main__':
     app.run(port=5000, debug=True, host='0.0.0.0') 