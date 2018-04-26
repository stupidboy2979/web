from django.http import HttpResponse
# from django.shortcuts import render
import time


# Create your views here.
def hello(request):
    str = '<title>Hello wrold!!!</title><h>你好%s</h>' % (time.time())
    return HttpResponse(str)
