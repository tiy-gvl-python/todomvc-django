
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from todo.views import GetCreateTodo, DeleteUpdateRetrieve

urlpatterns = [
    url(r'^todos/$', GetCreateTodo.as_view(), name="get_create"),
    url(r'^todos/(?P<pk>\d+)/', DeleteUpdateRetrieve.as_view(), name="delete_update"),
]