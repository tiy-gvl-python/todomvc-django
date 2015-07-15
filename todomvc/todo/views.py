from django.shortcuts import render
from rest_framework import generics
from todo.models import Todo
from rest_framework import serializers
# Create your views here.



class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        ordering = ('-title')


class ListCreateTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DeleteUpdateRetrieveTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer






