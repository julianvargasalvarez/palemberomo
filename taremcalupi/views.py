from django.http import HttpResponse
from django.views.generic.base import View as Controller
from django.shortcuts import render_to_response
from models import User

class HomeController(Controller):
    def get(self, request):
        usuarios = User.objects.all()
        return render_to_response("home.html", {'usuarios': usuarios})

class AlgoController(Controller):
    def get(self, request):
        usuario = {'nombre': 'julian',
                'apellido':'vargas',
                'lenguajes': ['python', 'ruby', 'sml', 'javascript'],
                'telefono':"123445",
                'sistemas_operativos':['windows','linux', 'osx']
                }
        
        return render_to_response("algo.html", usuario)
