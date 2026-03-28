from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.


def display(request):
    return HttpResponse("<h1>My first django App!!</h1>")


def displayDatetime(request):
    dt = datetime.datetime.now()
    s = "<b> Current Date and Time:<b/>" + str(dt)
    return HttpResponse(s)