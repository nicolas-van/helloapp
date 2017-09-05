from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from . import models

def index(request):
    return render(request, 'hello.html', { "name": "stranger" })

def get_name(request, name_id):
    name = get_object_or_404(models.Name, id = name_id)
    return render(request, 'hello.html', { "name": name.name })
