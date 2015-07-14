from django.conf.urls import  url
from todo.views import GetCreateTodo, DeleteUpdateRetrieve

urlpatterns = [
    url(r'^todos/$', GetCreateTodo.as_view(), name="get_create"),
    url(r'^todos/(?P<pk>\d+)/$', DeleteUpdateRetrieve.as_view())


]
