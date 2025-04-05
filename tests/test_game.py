import unittest
from game import generate_number, check_guess, play_sound

class TestNumberGuessingGame(unittest.TestCase):

    def test_generate_number(self):
        """Test if the number generated is within the specified range."""
        num = generate_number(1, 100)
        self.assertTrue(1 <= num <= 100)

    def test_check_guess_correct(self):
        """Test if correct guess returns the right message."""
        self.assertEqual(check_guess(50, 50), "correct")

    def test_check_guess_too_low(self):
        """Test if lower guess returns 'too low'."""
        self.assertEqual(check_guess(30, 50), "too low")

    def test_check_guess_too_high(self):
        """Test if higher guess returns 'too high'."""
        self.assertEqual(check_guess(80, 50), "too high")

    def test_play_sound(self):
        """Test sound playback with mock (no actual sound required)."""
        try:
            play_sound("win.wav")
            self.assertTrue(True)
        except Exception:
            self.fail("Sound playback failed.")

if __name__ == '__main__':
    unittest.main()
