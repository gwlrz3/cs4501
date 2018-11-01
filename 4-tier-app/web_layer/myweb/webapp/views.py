from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.core import serializers
import requests
import urllib.parse
import exp_srvc_errors

import json


def home(request):

    return render(request, 'home.html')


def hall(request):
    req = requests.get("http://exp-api:8000/expapp/showall/hall")
    data = req.json()
    return render(request, 'hall.html', {'objects': data})


def advisor(request):
    req = requests.get("http://exp-api:8000/expapp/showall/advisor")
    data = req.json()
    return render(request, 'advisor.html', {'objects': data})


def student(request):
    req = requests.get("http://exp-api:8000/expapp/showall/student")
    data = req.json()
    return render(request, 'student.html', {'objects': data})


def manager(request):
    req = requests.get("http://exp-api:8000/expapp/showall/manager")
    data = req.json()
    return render(request, 'manager.html', {'objects': data})


def room(request):
    req = requests.get("http://exp-api:8000/expapp/showall/room")
    data = req.json()
    return render(request, 'room.html', {'objects': data})


def lease(request):
    req = requests.get("http://exp-api:8000/expapp/showall/lease")
    data = req.json()
    return render(request, 'lease.html', {'objects': data})


def login(request):
    # If we received a GET request instead of a POST request
    if request.method == 'GET':
        # display the login form page
        next = request.GET.get('next') or reverse('home')
        return render('login.html', ...)

    # Creates a new instance of our login_form and gives it our POST data
    f = login_form(request.POST)

    # Check if the form instance is invalid
    if not f.is_valid():
      # Form was bad -- send them back to login page and show them an error
      return render('login.html', ...)

    # Sanitize username and password fields
    username = f.cleaned_data['username']
    password = f.cleaned_data['password']

    # Get next page
    next = f.cleaned_data.get('next') or reverse('home')

    # Send validated information to our experience layer
    resp = login_exp_api(username, password)

    # Check if the experience layer said they gave us incorrect information
    if not resp or not resp['ok']:
      # Couldn't log them in, send them back to login page with error
      return render('login.html', ...)

    """ If we made it here, we can log them in. """
    # Set their login cookie and redirect to back to wherever they came from
    authenticator = resp['resp']['authenticator']

    response = HttpResponseRedirect(next)
    response.set_cookie("auth", authenticator)

    return response

def create_listing(request):

    # Try to get the authenticator cookie
    auth = request.COOKIES.get('auth')

    # If the authenticator cookie wasn't set...
    if not auth:
      # Handle user not logged in while trying to create a listing
      return HttpResponseRedirect(reverse("login") + "?next=" + reverse("create_listing")

    # If we received a GET request instead of a POST request...
    if request.method == 'GET':
        # Return to form page
        return render("create_listing.html", ...)

    # Otherwise, create a new form instance with our POST data
    f = create_listing_form(request.POST)

    # ...

    # Send validated information to our experience layer
    resp = create_listing_exp_api(auth, ...)

    # Check if the experience layer said they gave us incorrect information
    if resp and not resp['ok']:
        if resp['error'] == exp_srvc_errors.E_UNKNOWN_AUTH:
            # Experience layer reports that the user had an invalid authenticator --
            #   treat like user not logged in
            return HttpResponseRedirect(reverse("login") + "?next=" + reverse("create_listing")

    # ...

    return render("create_listing_success.html", ...)