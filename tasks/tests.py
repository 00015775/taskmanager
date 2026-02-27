import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from tasks.models import Task, Tag


@pytest.fixture
def user(db):
    return User.objects.create_user(username='testuser', password='StrongPass123!')


@pytest.fixture
def logged_in_client(client, user):
    client.login(username='testuser', password='StrongPass123!')
    return client


@pytest.mark.django_db
class TestTasks:

    def test_task_model_creation(self, user):
        task = Task.objects.create(title='My Task', owner=user)
        assert task.title == 'My Task'

    def test_task_list_requires_login(self, client):
        response = client.get(reverse('task_list'))
        assert response.status_code == 302

    def test_user_can_create_task(self, logged_in_client):
        response = logged_in_client.post(reverse('task_create'), {
            'title': 'New Task',
            'description': 'Test',
            'priority': 'medium',
            'status': 'todo',
        })

        assert response.status_code == 302
        assert Task.objects.filter(title='New Task').exists()

    def test_user_can_edit_task(self, logged_in_client, user):
        task = Task.objects.create(title='Old Title', owner=user)

        response = logged_in_client.post(  # noqa: F841
            reverse('task_edit', kwargs={'pk': task.pk}),
            {
                'title': 'Updated Title',
                'priority': 'low',
                'status': 'done',
            }
        )

        task.refresh_from_db()
        assert task.title == 'Updated Title'

    def test_user_can_delete_task(self, logged_in_client, user):
        task = Task.objects.create(title='Delete Me', owner=user)

        response = logged_in_client.post(
            reverse('task_delete', kwargs={'pk': task.pk})
        )

        assert response.status_code == 302
        assert not Task.objects.filter(pk=task.pk).exists()


@pytest.mark.django_db
class TestTags:

    def test_user_can_create_tag(self, logged_in_client):
        response = logged_in_client.post(reverse('tag_list'), {
            'name': 'Work',
            'color': '#ff0000',
        })

        assert response.status_code == 302
        assert Tag.objects.filter(name='Work').exists()
