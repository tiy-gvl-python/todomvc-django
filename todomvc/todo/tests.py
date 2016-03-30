from django.test import TestCase
from todo.models import Todo

# Create your tests here.


class ListViewTests(TestCase):

    def setUp(self):
        self.hellotodo = Todo.objects.create(title="Hello")
        self.hitodo = Todo.objects.create(title="Hi")

    def test_todo_list(self):
        response = self.client.get("api/todos/")
        print(response)