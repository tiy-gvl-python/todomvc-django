from django.shortcuts import render

# Create your views here.
from rest_framework import generics, serializers
from todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo


class ListCreateTodoView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class RetrieveUpdateDestroyTodoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer