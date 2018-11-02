from django.test import TestCase, Client
from django.urls import reverse
from modelapp import models
import datetime



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

class CreateUserTests(TestCase):
    def test_success_response(self):
        response = self.client.post('/modelapp/user/create', data = {
            'username' : 'admin',
            'password' : '12345',
        })
        self.assertEquals(response.status_code, 200)

class ListUserTests(TestCase):
    def test_success_response(self):
        response = self.client.get('/modelapp/user/list')
        self.assertEquals(response.status_code, 200)

class DeleteUserTests(TestCase):
    def test_success_response(self):
        u = models.User()
        u.username = 'admin'
        u.password = '12345'
        u.save()
        response = self.client.post('/modelapp/user/delete/1')
        self.assertEquals(response.status_code, 200)

class AuthenticateUserTests(TestCase):
    def test_success_response(self):
        u = models.User()
        u.username = 'admin'
        u.password = '12345'
        u.save()
        response = self.client.post('/modelapp/user/authenticate', data = {
            'username' : 'admin',
            'password' : '12345',
        })
        self.assertEquals(response.status_code, 200)

class ListAuthenticatorTests(TestCase):
    def test_success_response(self):
        response = self.client.get('/modelapp/authenticator/list')
        self.assertEquals(response.status_code, 200)

class CreateAuthenticatorTests(TestCase):
    def test_success_response(self):
        response = self.client.post('/modelapp/authenticator/create', data = {
            'username' : 'admin',
            'password' : '12345',
        })
        self.assertEquals(response.status_code, 200)

class DeleteAuthenticatorTests(TestCase):
    def test_success_response(self):

        u = models.User()
        u.username = 'admin'
        u.password = '12345'
        u.save()
        auth = models.Authenticator()
        auth.user = 1
        auth.authenticator = 'asdffg'
        auth.date_created = datetime.datetime.now()
        response = self.client.post('/modelapp/authenticator/delete/asdffg')
        self.assertEquals(response.status_code, 200)
