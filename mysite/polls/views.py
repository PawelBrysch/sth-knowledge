from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    print("JESTEM TUTAJ")
    return HttpResponse("Hello, world. You're at the polls index.")
