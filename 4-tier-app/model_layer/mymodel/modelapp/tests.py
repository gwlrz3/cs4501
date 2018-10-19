from django.test import TestCase, Client
from django.urls import reverse

class ListStudentTestCase(TestCase):
    def setUp(self):
        pass #nothing to set up

     def success_response(self):
        response = self.client.get('/hall/list')
        self.assertEquals(response.status_code, 200)

    #tearDown method is called after each test
    def tearDown(self):
        pass #nothing to tear down