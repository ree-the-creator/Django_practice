from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Welcome to the Django Project")


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


# Please add: An about page that shows some text about yourself
def about(request):
    return HttpResponse("I'm resego and i'm learning how to code")
