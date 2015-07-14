from django.shortcuts import render

from rest_framework import generics, serializers
from .models import Todo



class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo




class GetCreateTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DeleteUpdateRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer