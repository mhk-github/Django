###############################################################################
# FILE     : tests.py
# SYNOPSIS : All Django tests are found here.
# LICENSE  : MIT
###############################################################################


###############################################################################
# IMPORTS
###############################################################################

import json

from django.test import TestCase, Client
from django.urls import reverse

from .models import Todo


###############################################################################
# CLASSES
###############################################################################

class TodoTestModel(TestCase):
    """Model to test using a database."""
    
    def setUp(self):
        Todo.objects.create(
            task='abc',
            location='London'
        )
        Todo.objects.create(
            task='def',
            location='Melbourne'
        )

    def test_todo_model_task_found_correctly(self):
        task_1 = Todo.objects.get(task='abc')
        task_2 = Todo.objects.get(task='def')
        self.assertEqual(task_1.location, 'London')
        self.assertEqual(task_2.location, 'Melbourne')
        
    def test_todo_model_task_create(self):
        Todo.objects.create(
            task='ghi',
            location='Vladivostok'
        )
        self.assertTrue(Todo.objects.filter(task='ghi').exists())
        
    def test_todo_model_task_starts_undone(self):
        task_1 = Todo.objects.create(
            task='jkl',
            location='Paris'
        )
        self.assertFalse(task_1.done)

    def test_todo_model_task_update(self):
        task_1 = Todo.objects.create(
            task='mno',
            location='London'
        )
        task_1.task = 'pqr'
        task_1.save()
        self.assertFalse(Todo.objects.filter(task='mno').exists())
        self.assertTrue(Todo.objects.filter(task='pqr').exists())
        
    def test_todo_model_task_delete(self):
        task_1 = Todo.objects.create(
            task='stu',
            location='Paris'
        )
        self.assertTrue(Todo.objects.filter(task='stu').exists())
        task_1.delete()
        self.assertFalse(
            Todo.objects.filter(task='stu').exists()
        )

    def test_todo_model_task_gives_valid_string(self):
        task_1 = Todo.objects.get(task='abc')
        task_2 = Todo.objects.get(task='def')
        string_1 = f"{task_1}"
        string_2 = f"{task_2}"
        self.assertIn('abc', string_1)
        self.assertIn('def', string_2)


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
        self.show_url = reverse('todos:show', args = ['1'])
        self.create_url = reverse('todos:create')
        self.update_url = reverse('todos:update', args = ['1'])
        self.delete_url = reverse('todos:delete', args = ['3'])
    
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
        });
        self.assertEquals(response.status_code, 302)
        self.assertTrue(Todo.objects.filter(task='GHI').exists())
        
    def test_todo_view_update_POST(self):
        response = self.client.post(self.update_url, {
            'task': 'JKL'
        });
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
