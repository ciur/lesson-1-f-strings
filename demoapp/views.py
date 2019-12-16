import logging

from django.http import Http404
from django.shortcuts import render

from demoapp.models import Person


logger = logging.getLogger(__name__)


def profile(request, id):

    message = ("Some error message", 255)

    logger.debug(f"id={id}")

    try:
        person = Person.objects.get(pk=id)
    except Person.DoesNotExist:
        raise Http404("Profile not found")

    logger.debug(f"msg={message}")

    return render(
        request,
        'demoapp/profile.html',
        {'person': person}
    )
