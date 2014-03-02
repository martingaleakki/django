from django.conf.urls import patterns, url
from investor import views

urlpatterns = patterns('',
        url(r'^register/', views.createInvestor, name='index'))