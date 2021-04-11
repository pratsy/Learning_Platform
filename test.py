# test_bucketlist.py
import unittest
import os
import json
from app import create_app, db


class LearningPlatformTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.user_data = {'user_id': 'L1','user_name': 'pratsy', 'email': 'pratsy@gmail.com', 'user_type': 'student' }

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_user_creation(self):
        """Test API can create a registration (POST request)"""
        res = self.client().post('/doRegistration/', data=self.user_data)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Testing Application', str(res.data))

    def test_api_can_get_all_users(self):
        """Test API can get a registration (GET request)."""
        res = self.client().post('/doRegistration/', data=self.user_data)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/getRegistration/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Testing Application', str(res.data))


    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()