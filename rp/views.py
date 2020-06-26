from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def register(request):
    return HttpResponse("Register")

def auth(request):
    return HttpResponse("Auth")

def find_a_roleplayer(request):
    return HttpResponse("There will be profiles")

def edit_page(request):
    return HttpResponse("EditPage")

def suggest_a_fandom(request):
    return HttpResponse("Suggest a fandom")
