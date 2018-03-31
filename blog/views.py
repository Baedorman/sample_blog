# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at my blog.")
    name = "Baedorman"
    return render(request, "index.html", {"name" : name})
