from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_app2(request):
    return HttpResponse("<h1>app2 first view function1</h1>")

def second_app2(request):
    return HttpResponse("<h1>app2 second view function2</h1>")