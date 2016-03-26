from django.test import TestCase
from todo.models import Todo
from django.core.urlresolvers import reverse
# Create your tests here.



class GetAndPostTest(TestCase):


    def setUp(self):
        self.clean = Todo.objects.create(title='You need to clean')
        self.run = Todo.objects.create(title='go run')
        self.homework = Todo.objects.create(title='do your homework asshole')


    def test(self):
        response = self.client.get('get_and_post')
        self.assertTrue(response)
        self.fail()


class EverythingTest(TestCase):

    def setUp(self):
        self.clean = Todo.objects.create(title='You need to clean')
        self.run = Todo.objects.create(title='go run')
        self.homework = Todo.objects.create(title='do your homework asshole')


    def test(self):
        response = self.client.get('api:put_and_delete')
        print(response)
        self.assert("go run" in str(response.context))