from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json
from .models import CarMake,CarModel
from .restapis import get_dealers_from_cf, get_request
# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
def about(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/about.html', context)


# Create a `contact` view to return a static contact page
def contact(request):
    context = {}
    if request.method == "GET":
        return render(request, "djangoapp/contact.html", context)

# Create a `login_request` view to handle sign in request
def login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('djangoapp:index')
        else:
            context['message'] = "Invalid username or password."
            return render(request, 'djangoapp/index.html', context)
    else:
        return render(request, 'djangoapp/index.html', context)

# Create a `logout_request` view to handle sign out request
def logout(request):
    logout(request)
    return redirect('djangoapp:index')

# Create a `registration_request` view to handle sign up request
def registration(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'djangoapp/registration.html', context)
    elif request.method == 'POST':
        # Check if user exists
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except:
            logger.error("New user")
        if not user_exist:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            login(request, user)
            return redirect("djangoapp:index")
        else:
            context['message'] = "User already exists."
            return render(request, 'djangoapp/registration.html', context)

# Update the `get_dealerships` view to render the index page with a list of dealerships



# Create a `get_dealer_details` view to render the reviews of a dealer
def get_dealerships(request):
    context={}
    if request.method == "GET":
        url = "https://us-south.functions.appdomain.cloud/api/v1/web/80e2d00c-0e24-4e32-99b7-f13b93e447ec/default/get-dealerships"
        # Get dealers from the URL
        dealerships = get_dealers_from_cf(url)
        context["dealership_list"] = dealerships
        # Return a list of dealer short name
        return render(request, 'djangoapp/index.html', context)
# ...
def get_dealer_details(request, dealer_id):
    context={}
    if request.method=="GET":
        url="https://us-south.functions.cloud.ibm.com/api/v1/namespaces/80e2d00c-0e24-4e32-99b7-f13b93e447ec/actions/get-review"
        reviews=get_dealer_reviews_from_cf(url)
        context={reviews}
        review_details=' '.join([review.id for review in reviews])
        for review in review_details:
            print(review.sentiment)
        return render(request, 'djangoapp/dealer_details.html', context)
# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...
def add_review(request, dealer_id):
    context={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['psw']
        user=authenticate(username=username,password=password)
        if user is not None:
            review["time"]=datetime.utcnow().isoformat()
            review["dealership"]=11
            review["review"]="This is a great car dealer"
            review["name"]="dealer1"

            json_payload["review"]=review
            review_response=post_request(url,json_payload, dealer_id=dealer_id)
            print(review_response)
            return HttpResponse(review_response)
    if request.method=="GET":
        json_payload["review"]=review
        review["time"]=datetime.utcnow.isoformat(review["time"])
        review["purchase"]=car.year.strftime("%Y")
        redirect("djangoapp:dealer_details", dealer_id=dealer_id)





