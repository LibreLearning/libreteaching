# Create your views here.

from django.http import HttpResponse,HttpResponseNotFound
from content.models import Pages

def show_content(request, resource):
    if request.user.is_authenticated():
        logged = "Logged in as " + request.user.username + '. <a href="/logout">Logout</a>'
    else:
        logged = 'Not logged in. <a href="/login">Login</a>'
    if request.method == 'GET':
        try:
            record = Pages.objects.get(name=resource)
            return HttpResponse(logged + '</br><hr> ' + record.page)
        except Pages.DoesNotExist:
            return HttpResponseNotFound(logged + '</br><hr>' + 'Page not found: /%s.' % resource)
    elif request.method == 'PUT':
        try:
            record = Pages.objects.get(name=resource)
            record.page = request.raw_post_data
        except Pages.DoesNotExist:
            record = Pages(name=resource, page=request.raw_post_data)
        record.save()
        return HttpResponse(request.raw_post_data)

