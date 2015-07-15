from django.core.urlresolvers import reverse
from django.shortcuts import render
from todo.models import Todo
from rest_framework import serializers, generics


class MySerializer(serializers.ModelSerializer):

  #  ser = serializers.SerializerMethodField()

   # def get_ser(self, obj):
    #    return reverse('put_and_delete', kwargs={'pk': obj.pk})

    class Meta:
        model = Todo
       # fields = ['pk', 'title', 'completed', 'order', 'ser']


class GetAndPost(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = MySerializer


class Everything(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = MySerializer