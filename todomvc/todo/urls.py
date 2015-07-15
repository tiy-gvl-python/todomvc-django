
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from todo.views import ListCreateTodo, DeleteUpdateRetrieveTodo


urlpatterns = [
    url(r'^todos/$',ListCreateTodo.as_view(), name="get_create"),
    url(r'^todos/(?P<pk>\d+)/$', DeleteUpdateRetrieveTodo.as_view(), name="delete_update"),


    ]