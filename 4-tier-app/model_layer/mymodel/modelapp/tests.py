from django.test import TestCase, Client
from django.urls import reverse

class ListStudentTests(TestCase):

     def success_response(self):
        response = self.client.get('/student/list')
        self.assertEquals(response.status_code, 200)