from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

from raven.contrib.django.models import client

import random
import logging

class RandomError(Exception):
    def __init__(self, message):
        self.message = message

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    try:
        if random.randint(0,1) == 1:
            logger = logging.getLogger(__name__)
            logger.debug('There is a 50% chance this action raises an error')
            raise RandomError('There is a chance this action raises an error')
        else:
            return render(request, "index.html")
    except:
        client.captureException()


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
