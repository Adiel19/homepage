from django.shortcuts import render

def home(request):
    return render(request, 'say_hi/home.html')
