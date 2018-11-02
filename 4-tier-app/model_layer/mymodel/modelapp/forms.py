from modelapp import models
from django.forms import ModelForm


class HallForm(ModelForm):
    class Meta:
        model = models.Hall
        fields = ['name', 'address']


class AdvisorForm(ModelForm):
    class Meta:
        model = models.Advisor
        fields = ['name', 'gender', 'birthdate', 'address', 'phone_no', 'department', 'position']


class ManagerForm(ModelForm):
    class Meta:
        model = models.Manager
        fields = ['name', 'gender', 'birthdate', 'address', 'phone_no', 'hall']


class StudentForm(ModelForm):
    class Meta:
        model = models.Student
        fields = ['name', 'gender', 'birthdate', 'address', 'phone_no', 'department', 'advisor']


class RoomForm(ModelForm):
    class Meta:
        model = models.Room
        fields = ['hall', 'room_no', 'price']


class LeaseForm(ModelForm):
    class Meta:
        model = models.Lease
        fields = ['student', 'room', 'start_date', 'end_date']


class UserForm(ModelForm):
    class Meta:
        model = models.User
        fields = ['username', 'password']


class AuthenticatorForm(ModelForm):
    class Meta:
        model = models.Authenticator
        fields = ['authenticator', 'user', 'date_created']

