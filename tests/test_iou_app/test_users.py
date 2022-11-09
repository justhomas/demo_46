import pytest
from iou.models import IouUser
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


@pytest.mark.django_db
class UserTests(APITestCase):
    def test_user_create(self):
        """
        Ensure we can create a new users.
        """
        url = reverse('iouuser-list')
        data = {'name': 'Justin'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(IouUser.objects.count(), 1)
        self.assertEqual(IouUser.objects.get().name, 'Justin')
    
    def test_user_create_duplicate_name(self):
        """
        Ensure that two users with same name cannot be created.
        """
        url = reverse('iouuser-list')
        data = {'name': 'Justin'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(IouUser.objects.count(), 1)
        self.assertEqual(IouUser.objects.get().name, 'Justin')

        # Trying to create second user with same name
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(IouUser.objects.count(), 1)
