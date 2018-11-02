from django.db import models
from django.utils.timezone import datetime

class Staff(models.Model):
    name = models.CharField(max_length = 30)
    gender = models.CharField(max_length = 10)
    birthdate = models.CharField(max_length = 10)
    address = models.CharField(max_length = 50)
    phone_no = models.CharField(max_length = 30)
    
    class Meta:
        abstract = True


class Advisor(Staff):
    department = models.CharField(max_length = 30)
    position = models.CharField(max_length = 30)


class Student(models.Model):
    advisor = models.ForeignKey(Advisor, on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length = 30)
    gender = models.CharField(max_length = 10)
    birthdate = models.CharField(max_length = 10)
    address = models.CharField(max_length = 50)
    department = models.CharField(max_length = 30)
    phone_no = models.CharField(max_length = 30)


class Hall(models.Model): 
    name = models.CharField(max_length = 10)
    address = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class Manager(Staff):
    hall = models.ForeignKey(Hall, on_delete = models.CASCADE, null = True)


class Room(models.Model):
    hall = models.ForeignKey(Hall, on_delete = models.CASCADE, null = True)
    room_no = models.IntegerField()
    price = models.IntegerField()


class Lease(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE, null = True)
    room = models.ForeignKey(Room, on_delete = models.CASCADE, null = True)
    start_date = models.CharField(max_length = 30)
    end_date = models.CharField(max_length = 30)


class User(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)


class Authenticator(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    authenticator = models.CharField(primary_key = True, max_length = 100)
    date_created = models.DateTimeField(default=datetime.now)


