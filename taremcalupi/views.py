from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView 
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse

from models import User
from forms import UserForm

import json

class UserList(ListView):
    model = User
    template_name = 'user_list.html'

    #def render_to_response(self, context, **response_kwargs):
    #    response_kwargs['content_type'] = 'application/json'
    #    return HttpResponse(json.dumps({'saludo': 'hola mundo'}))

class UserCreate(CreateView):
    model = User
    form_class = UserForm
    template_name = 'user_create.html'
    success_url = reverse_lazy('user_list')

class UserUpdate(UpdateView):
    model = User
    template_name = 'user_create.html'
    success_url = reverse_lazy('user_list')

class UserDelete(DeleteView):
    model = User
    template_name = 'user_delete.html'
    success_url = reverse_lazy('user_list')
