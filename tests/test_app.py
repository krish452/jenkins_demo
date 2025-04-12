import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_contact_page(self):
        response = self.app.post('/contact', data={'name': 'John', 'message': 'Hello!'})
        self.assertIn(b'Thank you, John!', response.data)

if __name__ == '__main__':
    unittest.main()
