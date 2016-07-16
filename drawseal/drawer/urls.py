from django.conf.urls import patterns, include, url
import views

urlpatterns=[
    url(r'^demo2$', views.demo2),
    url(r'^demo1$', views.demo1),
    url(r'^ellipseFont$', views.ellipseFont),
]