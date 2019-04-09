import unittest

target = __import__('quickstart_ink')

class TestCalendar(unittest.TestCase):

    def test_sum(self):
        self.assertTrue(target.getGoogleCalendar())

if __name__ == '__main__':
    unittest.main()
