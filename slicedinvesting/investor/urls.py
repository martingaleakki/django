from django.conf.urls import patterns, url
from investor import views

urlpatterns = patterns('',
        url(r'^login/', views.loginInvestor, name='login'))