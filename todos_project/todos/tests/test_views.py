###############################################################################
# FILE     : test_views.py
# SYNOPSIS : All Django app tests for views are found here.
# LICENSE  : MIT
###############################################################################


###############################################################################
# IMPORTS
###############################################################################

from django.test import TestCase, Client
from django.urls import reverse

from todos.models import Todo


###############################################################################
# CLASSES
###############################################################################

class TodoTestView(TestCase):
    """View to test."""

    def setUp(self):
        self.todo_1 = Todo.objects.create(
            task='ABC',
            location='Paris'
        )
        self.todo_2 = Todo.objects.create(
            task='DEF',
            location='New York'
        )
        self.client = Client()
        self.list_url = reverse('todos:index')
        self.show_url = reverse('todos:show', args=['1'])
        self.create_url = reverse('todos:create')
        self.update_url = reverse('todos:update', args=['1'])
        self.delete_url = reverse('todos:delete', args=['3'])

    def test_todo_view_list_GET(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'todos/index.html')

    def test_todo_view_show_GET(self):
        response = self.client.get(self.show_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'todos/show.html')

    def test_todo_view_create_POST(self):
        response = self.client.post(self.create_url, {
            'task': 'GHI',
            'location': 'London'
        })
        self.assertEquals(response.status_code, 302)
        self.assertTrue(Todo.objects.filter(task='GHI').exists())

    def test_todo_view_update_POST(self):
        response = self.client.post(self.update_url, {
            'task': 'JKL'
        })
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'todos/update.html')

    def test_todo_view_delete_POST(self):
        Todo.objects.create(
            task='MNO',
            location='New York'
        )
        response = self.client.delete(self.delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'todos/delete.html')


###############################################################################
# END
###############################################################################
# Local variables:
# mode: python
# End:
