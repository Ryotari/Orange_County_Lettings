from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Profile


class ProfilesTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="User1",
            password="password123",
            email="User1@gmail.com"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city="Paris")

    def test_profiles_index(self):
        response = self.client.get(reverse('profiles:index'))
        assert response.status_code == 200
        assert b"<title>Profiles</title>" in response.content

    def test_profile_detail(self):
        response = self.client.get(reverse('profiles:profile', args=["User1"]))
        assert response.status_code == 200
        assert b"<title>User1</title>" in response.content

    def test_profile_model(self):
        assert str(self.profile) == self.user.username
