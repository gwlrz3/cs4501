from django.test import TestCase, Client
from django.urls import reverse


class ListStudentTests(TestCase):
    def test_success_response(self):
        response = self.client.get('/modelapp/student/list')
        self.assertEquals(response.status_code, 200)


class ListHallTests(TestCase):
    def test_success_response(self):
        response = self.client.get('/modelapp/hall/list')
        self.assertEquals(response.status_code, 200)


class ListManagerTests(TestCase):
    def test_success_response(self):
        response = self.client.get('/modelapp/manager/list')
        self.assertEquals(response.status_code, 200)


class ListAdvisorTests(TestCase):
    def test_success_response(self):
        response = self.client.get('/modelapp/advisor/list')
        self.assertEquals(response.status_code, 200)


class ListRoomTests(TestCase):
    def test_success_response(self):
        response = self.client.get('/modelapp/room/list')
        self.assertEquals(response.status_code, 200)


class ListLeaseTests(TestCase):
    def test_success_response(self):
        response = self.client.get('/modelapp/lease/list')
        self.assertEquals(response.status_code, 200)
