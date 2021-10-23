###############################################################################
# FILE     : test_models.py
# SYNOPSIS : All Django app tests for models are found here.
# LICENSE  : MIT
###############################################################################


###############################################################################
# IMPORTS
###############################################################################

from django.test import TestCase

from todos.models import Todo


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


###############################################################################
# END
###############################################################################
# Local variables:
# mode: python
# End:
