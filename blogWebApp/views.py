from django.shortcuts import render

def home(requests):
    return render(requests,"base.html")