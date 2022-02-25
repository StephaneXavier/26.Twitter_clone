from unittest import TestCase

import sqlalchemy
import os
from sqlalchemy import exc

from models import db, User, Message, Follows, Likes

os.environ['DATABASE_URL'] = 'postgresql://warbler-test'

from app import app
db.create_all()


class Models_test(TestCase):
    def setUp(self):
        db.drop_all()
        db.create_all()

        u = User.signup(username='username1',email='email1@gmail.com',
        password='password')
        u.id = self.uid
        db.session.commit()

        self.u = User.query.get(self.uid)

        self.client = app.test_client()


    def test_create_user(self):

