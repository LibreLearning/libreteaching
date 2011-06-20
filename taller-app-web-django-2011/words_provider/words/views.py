# Create your views here.

from django.http import HttpResponse,HttpResponseNotFound
import random

def gimmeword(request, resource):
    if resource == 'first':
        word = random.choice(["The table", "My uncle", "A book", "The road", "Music"])
    elif resource == 'second':
        word = random.choice(["talks", "knows", "thinks", "works", "runs", "eats"])
    elif resource == 'third':
        word = random.choice(["fast", "low", "far away", "hard", "in pijama", "while dances cha-cha-cha"])
    else:
        return HttpResponseNotFound('Page not found')
    return HttpResponse(word)

