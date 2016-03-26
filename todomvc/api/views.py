from django.core.urlresolvers import reverse
from django.shortcuts import render
from todo.models import Todo
from rest_framework import serializers, generics


class MySerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo


class GetAndPost(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = MySerializer


class Everything(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = MySerializer