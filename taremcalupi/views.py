from django.http import HttpResponse
from django.views.generic.base import View as Controller
from django.shortcuts import render_to_response

class HomeController(Controller):
    def get(self, request):
        usuarios = ["usuario1", "usuario2"]
        return render_to_response("home.html", {'usuarios': usuarios})

class AlgoController(Controller):
    def get(self, request):
        numeros = range(100)
        return render_to_response("algo.html", {'numeros': numeros})
