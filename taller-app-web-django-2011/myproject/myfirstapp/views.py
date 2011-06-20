# Create your views here.

from django.http import HttpResponse
def say_main(request):
     return HttpResponse('<h1>My First Application</h1>')
def say_hello(request):
     return HttpResponse('Hello!')
def say_bye_to(request, name):
     return HttpResponse('Bye %s'%name)
def say_number(request, number=0):
     return HttpResponse('Number: %s'%number)
