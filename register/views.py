from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    return render(request, "index.html")

def registered(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    models.Registration.objects.create(name=name, email=email)
    print(name)
    return render(request, "registered.html")