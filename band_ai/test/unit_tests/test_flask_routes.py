import unittest
from app import create_app

class FlaskRoutesTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to Band AI!", response.data)

    def test_simulate_route(self):
        response = self.client.get('/simulate')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"simulation started", response.data)
