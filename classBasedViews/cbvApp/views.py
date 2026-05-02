from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse



# Create your views here.

class GreetingsView(View):
    message = "Welcome to CBV demo!."
    def get(self, request):
        return HttpResponse(self.message)