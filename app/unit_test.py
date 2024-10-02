import unittest
from werkzeug import exceptions

import app
from app import app as flask_instance

class AppTestCase(unittest.TestCase):
    def test_when_x_is_1(self):
        res = app.next5(1).response.pop()
        res = float(res)
        self.assertEqual(res, 6)
    
    def test_when_x_is_neg10(self):
        res = app.next5(-10).response.pop()
        res = float(res)
        self.assertEqual(res, -5)
    
    def test_when_x_is_1dot5(self):
        res = app.next5(1.5).response.pop()
        res = float(res)
        self.assertEqual(res, 6.5)

if __name__ == "__main__":
    with flask_instance.app_context():
        unittest.main()