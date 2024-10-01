import unittest
from werkzeug import exceptions

import app
from app import app as flask_instance

class AppTestCase(unittest.TestCase):
    def test_when_x_is_17(self):
        res = app.is_prime(17).response.pop()
        res = res.decode("utf-8").strip() == 'true'
        self.assertEqual(res, True)
    
    def test_when_x_is_36(self):
        res = app.is_prime(36).response.pop()
        res = res.decode("utf-8").strip() == 'true'
        self.assertEqual(res, False)
    
    def test_when_x_is_13219(self):
        res = app.is_prime(13219).response.pop()
        res = res.decode("utf-8").strip() == 'true'
        self.assertEqual(res, True)

if __name__ == "__main__":
    with flask_instance.app_context():
        unittest.main()