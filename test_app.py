# import unittest
# from app import app

# class FlaskTestCase(unittest.TestCase):

#     def setUp(self):
#         self.app = app.test_client()
#         self.app.testing = True

#     def test_home_status(self):
#         response = self.app.get('/')
#         self.assertEqual(response.status_code, 200)

#     def test_about_status(self):
#         response = self.app.get('/about')
#         self.assertEqual(response.status_code, 200)

# if __name__ == "__main__":
#     unittest.main()
import unittest
from app import app

class JokeAppTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    # ✅ Test Home Route
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Random Joke', response.data)

    # ✅ Test About Page
    def test_about_page(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About JokeApp', response.data)

    # ✅ Test Invalid Route (important edge case)
    def test_404(self):
        response = self.client.get('/invalid')
        self.assertEqual(response.status_code, 404)

    # ✅ Test API Integration (basic check)
    def test_joke_api_response(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        # Check if setup or punchline exists
        self.assertTrue(
            b'?' in response.data or b'!' in response.data
        )

if __name__ == "__main__":
    unittest.main()