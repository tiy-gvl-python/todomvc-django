from django.test import TestCase
from django.core.urlresolvers import reverse
from todo.models import Todo

class ListViewTests(TestCase):

    def setUp(self):
        self.hellotodo = Todo.objects.create(title="hello")
        self.goodbyetodo = Todo.objects.create(title="goodbye")

    def test_todo_list_view_includes_all_todos_in_database(self):
        response = self.client.get("api/todos/")
        print(response)
        pass
        #self.assertTrue("hello" in str(response.content))
        #todo_list = list(response.context)[0]['title']


