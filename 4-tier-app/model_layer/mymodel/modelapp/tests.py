from django.test import TestCase, Client
from django.urls import reverse

class ListStudentTests(TestCase):

    def test_success_response(self):
        response = self.client.get('/hall/list')
        self.assertEquals(response.status_code, 200)

