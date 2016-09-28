'''
from django.test import TestCase
from Todo.models import Todo


class ListViewTests(TestCase):

    def setUp(self):
        self.hellotodo = Todo.objects.create(title="Hello")
        self.hitodo = todo.objects.create(title="Hi")


    def test_todo_list(self):
        response = self.client.get("api/todos/")
'''


