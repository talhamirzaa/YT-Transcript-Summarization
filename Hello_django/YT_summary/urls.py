from django import urls
#from django.conf.urls import url
from django.contrib import admin 
from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.urls import include, re_path

#app_name = 'YT_summary'
urlpatterns = [
    #path("", views.index, name="index"),
    path('admin/', admin.site.urls),  
    path('index/', views.index),  
    path('wait/', TemplateView.as_view(template_name="data.html")),
    
    #actual
    #path('', TemplateView.as_view(template_name="index.html")),
    #path('', views.new,name="hello"),
    path('show', views.disp,name="test"),

    #testing from video
    re_path(r'^btn', views.button),
    re_path(r'^external', views.external),

    #my try
    re_path(r'pop', views.pop),
    re_path(r'call', views.call),

    #with nltk
    re_path(r'^disp', views.disp),
    re_path(r'^invok', views.invok),

    #format with nltk
    re_path(r'^$', views.srch),
    re_path(r'^get_sum', views.get_sum),

    # for test(success)
    path('hell', views.h,name="hello"),
    path('hi', views.s,name="any"),
   
    
]