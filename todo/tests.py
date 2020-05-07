from django.test import TestCase, Client
from django.urls import reverse
from .models import Task


class TaskModelTests(TestCase):

    def test_create_task(self):
        self.assertEqual(Task.objects.count(), 0)
        task = Task.objects.create(title='test')

        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(task.title, 'test')
        self.assertFalse(task.completed)


class ViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.task = Task.objects.create(title='test')

    def test_get_response(self):
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_create_task(self):
        self.assertEqual(Task.objects.count(), 1)
        data = {'title': 'new task'}
        response = self.client.post(reverse('list'), data)
        self.assertEqual(response.status_code, 302)
        new_task = Task.objects.get(title='new task')
        self.assertEqual(new_task.title, 'new task')
        self.assertFalse(new_task.completed)
        self.assertEqual(Task.objects.count(), 2)

    def test_update_task(self):
        self.assertEqual(Task.objects.count(), 1)
        data = {
            'title': 'new task',
            'completed': True,
            'pk': 1,
            'update': 1
        }
        response = self.client.post(reverse('list'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)
        self.assertFalse(Task.objects.filter(title__exact='test'))
        self.assertTrue(Task.objects.filter(title__exact='new task'))
        updated_task = Task.objects.get(title='new task')
        self.assertTrue(updated_task.completed)

    def test_delete_task(self):
        self.assertEqual(Task.objects.count(), 1)
        data = {
            'pk': 1,
            'delete': 1
        }
        response = self.client.post(reverse('list'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)
