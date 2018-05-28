from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from indexPage.models import *


# Create your views here.
def hello(request, name, message):
    str = '<title>Hello wrold!!!</title><h>%s你好</h><h>%s</h>' % (name, message)
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


def companies_list(request, location='洪山',p=0):
    locations = ['洪山',
                 '营房村',
                 ]
    companies = Company.objects.filter(location=location)
    return render(request, 'companies.html', {
        'companies': companies,
                                              'location_list': locations,
                                              'location': location,
                                              })


def company_detail(request, company_name):
    # company = get_object_or_404(Company, name=name)
    return render(request, 'detail.html', {'company': company_name})


def new_company(request, location='洪山'):
    if request.method == 'POST':
        company = request.POST
        # print(company['Name'])
        return redirect('detail', company_name=company['Name'])
    if location == '洪山':
        locations = ['洪山', '徐东', ]
    else:
        locations = ['营房村', '合作路', ]
    return render(request, 'new_company.html', {'location': location, 'locations': locations})

