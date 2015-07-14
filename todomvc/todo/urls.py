from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from .views import GetCreateView, DeleteUpdateRetrieve

urlpatterns = [
    url(r'^todos/$', GetCreateView.as_view(), name="get_create"),
    url(r'^todos/(?P<pk>\d+)/', DeleteUpdateRetrieve.as_view(), name="doesn't_matter"),

]
