# foodtrackerapp/views.py
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html', context=None)