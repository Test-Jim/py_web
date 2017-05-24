"""DjangoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from views import *
from app.views import *
import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^helloworld/', helloworld),
    url(r'^current_datetime/', current_datetime),
    url(r'^search_form/', search_form),
    # url(r'^search/', search),
    # url(r'^AddInStockBill/', AddInStockBill),
    url(r'^success/', success),
    # url(r'^AddItem/', AddItem),
    url(r'^index/', index),
    url(r'^login/', login),
    url(r'^update/', update),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_URL }),
]
