from django.http import Http404
from django.shortcuts import render

from demoapp.models import Person


def profile(request, id):

    try:
        person = Person.objects.get(pk=id)
    except Person.DoesNotExist:
        raise Http404("Profile not found")

    return render(
        request,
        'demoapp/profile.html',
        {'person': person}
    )


def stats(request, id):
    try:
        person = Person.objects.get(pk=id)
    except Person.DoesNotExist:
        raise Http404("Person not found")

    return render(
        request,
        'demoapp/stats.html',
        {'person': person}
    )

