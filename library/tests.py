from django.test import SimpleTestCase
from rest_framework.test import APIClient

class ValidateView(SimpleTestCase):
    
    def test_return_after_create(self):
        client = APIClient()
        res = client.get('/api/books/')
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            res.data,
            [{"id":1,"first_name":"Marcus","last_name":"Aurelius","biography":""}]
        )