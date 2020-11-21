import unittest
import requests
from app import app

# Creating a basic test case
class BasicTestCase(unittest.TestCase):
    def test(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')

        # Make sure the app returns the status code 200(OK)
        self.assertEqual(response.status_code, 200)

        # Inputs
        city = input("Enter Valid City: ")
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=API_KEY')
        self.assertEqual(response.status_code, 200)

        city = input("Enter Invalid City: ")
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=API_KEY')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
