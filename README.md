# First-Project
First project with QA


This project consists of information about common herbs and their cultivation. The user selects from choices in order that the web app will provide information depending on the combination. There are currently five herbs to get information from, and the user can select from 'sowing herbs', 'harvesting herbs', and the 'lifespan' of those herbs. The page will then return the requested information once the request has been submitted. 

A database will also be created through the create.py file, containing information on the plants, their lifecycle, best months to sow them, best months to harvest them, and their lifespan.

Lines 16-18 of app.py file contains three dictionaries, which provide data for both the website app, and the SQL tables created. In create.py file, the dictionaries have been imported so that the coding is cleaner and less strings are used. Three lists on lines 7-9 were made in order to neaten the 

This project was initially created to be a 'Plant Nursery'; somewhere customers could buy/leave their plants, get detailed information on the plants, and collect the plants when they are ready for collection. 

Create - I will create three tables in a new record in the SQL database. The tables, 'Herbs', 'Patrons' and 'Nursing' will consist of the following attributes: 

  Herbs: id pk, plant_name, genus, lifecycle, season_to_sow, season_to_harvest, lifespan
  Patrons: id pk, first_name, last_name, email_address
  Nursing: id pk, patrons_id fk, herbs_id fk

All of the forms in this SQL database will be 'NOT NULL'. 

Line 16-18 of app.py file contains three dictionaries, which provide data for both the website app, and the SQL tables created. In create.py file, the dictionaries have been imported so that the coding is cleaner and less strings are used. 

Read - Users of this app will be able to retrieve information on their plants' lifecycles, genus, when the plants are best sown, when the plants are best harvested. 


Update - The database will be updated with information on the patrons, information about common plants, and information on the plants that the 'patron' is currently cultivating. 


Delete - I deleted some of the initial attributes in my table and some code in order to tidy the code in the python file. I deleted the 'Nursery' concept of the project as I felt I would not be able to complete it in time; a possible improvement to be made. 
