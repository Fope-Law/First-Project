from flask import url_for
from flask_testing import TestCase
from app import app, db, Herbs, Patrons, Nursery 

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False)
        return app

    def setUp(self):
        db.create_all()
        sample1 = Patrons(first_name="Tola", last_name="Olufunmi", email_address="Tola@Olufunmi.test.uk")
        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

