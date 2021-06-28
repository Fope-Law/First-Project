from app import db, Herbs, Patrons, Nursery
from app import lifespan, sowing_season, harvest_season

db.drop_all()
db.create_all() 

herbs = ["Oregano", "Parsley", "Rosemary", "Sage", "Thyme"]
genus = ["Origanum", "Petroselinum", "Salvia", "Thymus"]
lifecycle = ["Annual", "Biennial", "Perennial"]


plant1 = Herbs(plant_name = herbs[0], 
    genus = genus[0], 
        lifecycle = lifecycle[2],
            season_to_sow = sowing_season["oregano"],
                season_to_harvest = harvest_season["oregano"],
                    lifespan = lifespan["oregano"])
plant2 = Herbs(plant_name = herbs[1], 
    genus = genus[1], 
        lifecycle = lifecycle[1],
            season_to_sow = sowing_season["parsley"],
                season_to_harvest = harvest_season["parsley"],
                    lifespan = lifespan["parsley"])
plant3 = Herbs(plant_name = herbs[2], 
    genus = genus[2], 
        lifecycle = lifecycle[2],
            season_to_sow = sowing_season["rosemary"],
                season_to_harvest = harvest_season["rosemary"],
                    lifespan = lifespan["rosemary"])
plant4 = Herbs(plant_name = herbs[3], 
    genus = genus[2], 
        lifecycle = lifecycle[2],
            season_to_sow = sowing_season["sage"],
                season_to_harvest = harvest_season["sage"],
                    lifespan = lifespan["sage"])
plant5 = Herbs(plant_name = herbs[4], 
    genus = genus[3], 
        lifecycle = lifecycle[2],
            season_to_sow = sowing_season["thyme"],
                season_to_harvest = harvest_season["thyme"],
                    lifespan = lifespan["thyme"])

db.session.add(plant1)
db.session.add(plant2)
db.session.add(plant3)
db.session.add(plant4)
db.session.add(plant5)
db.session.commit()

patron1 = Patrons(first_name = 'Femi', last_name = 'Ogunyemi', email_address = 'femitest@try.co.uk')
patron2 = Patrons(first_name = 'Tiwa', last_name = 'Savage', email_address = 'tiwa_slay@try.co.uk')
patron3 = Patrons(first_name = 'Rotimi', last_name = 'Oluwa', email_address = 'rotest213@try.co.uk')

db.session.add(patron1)
db.session.commit()

order1 = Nursery(herb = plant3, patron = patron1)
order2 = Nursery(herb = plant1, patron = patron2)
order3 = Nursery(herb = plant2, patron = patron2)
order4 = Nursery(herb = plant5, patron = patron3)
order5 = Nursery(herb = plant4, patron = patron2)

db.session.add(order1)
db.session.add(order2)
db.session.add(order3)
db.session.add(order4)
db.session.add(order5)
db.session.commit()
