from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_app1(request):
    return HttpResponse("<h1>app1 first view function1</h1>")


def second_app1(request):
    return HttpResponse("<h1>app1 second view function2</h1>")