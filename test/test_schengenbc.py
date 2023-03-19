import unittest
from src import schengenbc


class MyTestCase(unittest.TestCase):
    def test_countries(self):
        print(schengenbc.get_country('Austria'))
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
