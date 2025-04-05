import unittest
from app import app  # Import your Flask app

class NumberGuessingGameTestCase(unittest.TestCase):

    def setUp(self):
        # Creates a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Number Guessing Game', response.data)

    def test_setup_get(self):
        response = self.app.get('/setup')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Play Now', response.data)

    def test_setup_post_redirects_to_play(self):
        response = self.app.post('/setup', data=dict(
            player_name='TestUser',
            min_num=1,
            max_num=50,
            difficulty='easy'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Guess the Number', response.data)

    def test_play_get_without_session_redirects(self):
        response = self.app.get('/play', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Player Name:', response.data)

    def test_reset_route(self):
        response = self.app.get('/reset', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Number Guessing Game', response.data)

if __name__ == '__main__':
    unittest.main()
