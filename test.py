import unittest
from app import app

# Creating a basic test case
class BasicTestCase(unittest.TestCase):
    def test(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')

        # Make sure the app returns the status code 200(OK)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()