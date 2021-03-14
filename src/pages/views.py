from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage_view(request, *args, **kwargs):
    print(request.user)
    print(args, kwargs)
    # return HttpResponse("<h1>hello world</h1>")
    return 

def contact_view(*args, **kwargs):
    return HttpResponse("<h1>contant page</h1>")

def carrer_view(*args, **kwargs):
    return HttpResponse("<h1>contant page</h1>")