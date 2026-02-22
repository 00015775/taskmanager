import pytest
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.mark.django_db
class TestAccounts:

    # def test_register_page_loads(self, client):
    #     response = client.get(reverse('register'))
    #     assert response.status_code == 200

    def test_user_can_register(self, client):
        response = client.post(reverse('register'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
        })

        assert response.status_code == 302
        assert User.objects.filter(username='testuser').exists()

    def test_user_can_login(self, client, django_user_model):
        django_user_model.objects.create_user(
            username='testlogin',
            password='StrongPass123!'
        )

        response = client.post(reverse('login'), {
            'username': 'testlogin',
            'password': 'StrongPass123!',
        })

        assert response.status_code == 302

    def test_profile_requires_login(self, client):
        response = client.get(reverse('profile'))
        assert response.status_code == 302


