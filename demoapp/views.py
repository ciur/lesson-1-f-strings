from django.shortcuts import render

# Create your views here.


def profile(request):
    render(request, 'demoapp/profile.html')


def stats(request):
    render(request, 'demoapp/stats.html')
