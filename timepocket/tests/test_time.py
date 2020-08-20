import unittest
from timepocket import hoursToMinSec


class TestSum(unittest.TestCase):

    def test_hoursToMinSec(self):
        self.assertEqual(hoursToMinSec(12.34), {
                         'hours': 12, 'minutes': 20, 'seconds': 23}, "Should return correct value")


if __name__ == '__main__':
    unittest.main()
