import json
import unittest

from app import app

class TestEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_subtract(self):
        data = {'x': 5, 'y': 3}
        response = self.app.post('/api/sub', json=data)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode())
        self.assertEqual(result['result'], 2)

    def test_multiply(self):
        data = {'x': 4, 'y': 2}
        response = self.app.post('/api/mul', json=data)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode())
        self.assertEqual(result['result'], 8)

    def test_divide(self):
        data = {'x': 6, 'y': 2}
        response = self.app.post('/api/div', json=data)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode())
        self.assertEqual(result['result'], 3)

    def test_divide_by_zero(self):
        data = {'x': 5, 'y': 0}
        response = self.app.post('/api/div', json=data)
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode())
        self.assertEqual(result['error'], 'Division by zero.')

if __name__ == '__main__':
    unittest.main()