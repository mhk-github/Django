###############################################################################
# FILE     : tests.py
# SYNOPSIS : All Django tests are found here.
# LICENSE  : MIT
###############################################################################


###############################################################################
# IMPORTS
###############################################################################

from django.test import TestCase

from .models import Todo


###############################################################################
# CLASSES
###############################################################################

class TodoTestCase(TestCase):
    """Model to test using a database."""
    
    def setUp(self):
        Todo.objects.create(task='Test task 1', location='London')
        Todo.objects.create(task='Test task 2', location='Melbourne')

    def test_todo_task_found_correctly(self):
        task_1 = Todo.objects.get(task='Test task 1')
        task_2 = Todo.objects.get(task='Test task 2')
        self.assertEqual(task_1.location, 'London')
        self.assertEqual(task_2.location, 'Melbourne')

    def test_todo_task_has_temperature(self):
        task_1 = Todo.objects.get(task='Test task 1')
        task_2 = Todo.objects.get(task='Test task 2')
        self.assertIsNotNone(task_1.temperature)
        self.assertIsNotNone(task_2.temperature)

    def test_todo_task_starts_undone(self):
        task_1 = Todo.objects.get(task='Test task 1')
        task_2 = Todo.objects.get(task='Test task 2')
        self.assertFalse(task_1.done)
        self.assertFalse(task_2.done)

    def test_todo_task_gives_valid_string(self):
        task_1 = Todo.objects.get(task='Test task 1')
        task_2 = Todo.objects.get(task='Test task 2')
        string_1 = f"{task_1}"
        string_2 = f"{task_2}"
        self.assertIn('Test task 1', string_1)
        self.assertIn('Test task 2', string_2)


###############################################################################
# END
###############################################################################
# Local variables:
# mode: python
# End:
