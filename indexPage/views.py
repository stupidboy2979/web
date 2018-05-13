from django.http import HttpResponse
# from django.shortcuts import render
import time
from indexPage.models import Circuit, User


# Create your views here.
def hello(request):
    str = '<title>Hello wrold!!!</title><h>你好%s</h>' % (time.time())
    return HttpResponse(str)


def InitUser(request):
    c1 = Circuit(trunk=700, port='1-3-15-2', sgNum='201409879456')
    c1.save()
    c2 = Circuit(trunk=701, port='1-3-16-2', sgNum='201409879499')
    c2.save()
    u1 = User(name='武大吉奥', number='9898', portal='pra', das=9, dpc='10.56.9', )
    u1.save()
    u1.circuits.add(c1)
    u1.circuits.add(c2)

    return HttpResponse('<title>InitUser</title><h>InitUser Done!!!</h>')

