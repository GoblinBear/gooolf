import unittest

from golf import Golf


class TestGolf(unittest.TestCase):
    def test_run_monte_carlo(self):
        golf = Golf(1000, 5, 'ratings.txt')
        golf.run_monte_carlo()
        
        self.assertEqual(golf.number_of_golfer, 20)
