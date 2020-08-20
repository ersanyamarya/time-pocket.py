import unittest
from timepocket import hours_to_min_sec


class TestSum(unittest.TestCase):

    def test_hours_to_min_sec(self):
        self.assertEqual(hours_to_min_sec(12.34), {
                         'hours': 12, 'minutes': 20, 'seconds': 23}, "Should return correct value")


if __name__ == '__main__':
    unittest.main()
