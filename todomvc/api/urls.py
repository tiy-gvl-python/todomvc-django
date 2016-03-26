from django.conf.urls import url
from .views import GetAndPost, Everything

urlpatterns = [

    url(r'^todos/$', GetAndPost.as_view(), name='get_and_post'),
    url(r'todos/(?P<pk>\d+)$', Everything.as_view(), name='put_and_delete'),
]