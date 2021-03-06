from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Account', max_length=100)
    password = forms.CharField(label='Password', max_length=100)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Account', max_length=100)
    password = forms.CharField(label='Password', max_length=100)


class RoomForm(forms.Form):
    hall = forms.IntegerField(label='Hall')
    room_no = forms.IntegerField(label='Room')
    price = forms.IntegerField(label='Price')


class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=100)


