from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage_view(request, *args, **kwargs):
    print(request.user)
    print(args, kwargs)
    # return HttpResponse("<h1>hello world</h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def career_view(request, *args, **kwargs):
    my_context = {"my_text": "context testing in carrer", "my_email": "hello@gamil.com", "list": [1,2,3,4.4,5]}
    return render(request, "career.html", my_context)

def cat_view(request, *args, **kwargs):
    return render(request, "cat.html", {})