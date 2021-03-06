"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from indexPage.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<str:name>-<str:message>', hello, name='home'),
    path(r'InitUser/', InitUser),
    path(r'', companies_list, name='index'),
    path(r'companies/<str:location>/<int:p>', companies_list, name='companies'),
    path(r'companies/new/<str:location>', new_company, name='new_company'),
    path(r'detail/<str:company_name>/', company_detail, name='detail'),
]
