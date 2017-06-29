from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^homepage$', views.homepage , name ='home_page') ,
    url(r'^addsecret$', views.addsecret , name ='add_secret') ,
    url(r'^addlike/(?P<id>\d+)$', views.addlike , name ='add_like') ,
    url(r'^logout$', views.logout , name ='logout') 
    ]