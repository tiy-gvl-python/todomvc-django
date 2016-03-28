from django.core.urlresolvers import reverse
from django.test import TestCase
from todo.models import Todo
# Create your tests here.


class ListViewTests(TestCase):

    def setUp(self):
        self.hellotodo = Todo.objects.create(title="Hello")
        self.hitodo = Todo.objects.create(title="Hi")


    def test_todo_list(self):
        response = self.client.get("api/todos/")
        print(response.)
        self.fail()
        """self.assertTrue("Top gun" in str(response.content))
        movie_list = list(response.context)[0]['object_list']
        self.assertTrue(self.top_gun in movie_list)
        self.assertCountEqual(movie_list, Movie.objects.all())"""
