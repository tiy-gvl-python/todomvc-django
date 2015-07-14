from django.shortcuts import render
from rest_framework import generics
from rest_framework import serializers
from todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo


class ListCreateTodoView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class CreateDeleteTodoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer