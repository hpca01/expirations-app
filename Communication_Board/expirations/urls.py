"""Communication_Board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from . import views as exp_view

urlpatterns = [
    # url(r'^$', exp_view.home, name = 'home'),
    url(r'^$', exp_view.DrugListView.as_view() , name = 'drug_list'),
    url(r'^list/$', exp_view.DrugExpListView.as_view() , name = 'drug_exp_list'),
    url(r'^drug/new/$',exp_view.CreateDrugView.as_view(), name = 'drug_new'),
    url(r'^drug/(?P<pk>\d+)$', exp_view.DrugDetailView.as_view(), name = 'drug_detail'),
    url(r'^drug/(?P<pk>\d+)/delete$', exp_view.DrugDeleteView.as_view(), name = 'drug_delete'),
    url(r'^drug/(?P<pk>\d+)/expiration$', exp_view.CreateExpirationView.as_view(), name = 'add_expiration'),
    url(r'^drug/(?P<pk>\d+)/expiration/delete$', exp_view.ExpirationDeleteView.as_view(), name = 'expiration_delete'),
    url(r'^drug/(?P<pk>\d+)/barcode/new/$', exp_view.CreateBarcodeView.as_view(), name = 'add_barcode'),

]
