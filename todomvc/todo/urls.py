from django.conf.urls import url
from todo import views

urlpatterns = [
    url(r'^todos/$', views.ListCreateTodoView.as_view()),
    url(r'^todos/(?P<pk>\d+)/', views.CreateDeleteTodoView.as_view())
]