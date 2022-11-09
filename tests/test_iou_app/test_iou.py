import pytest
from iou.models import IouUser,Ledger
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import datetime,timezone


@pytest.mark.django_db
class IouTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up test users for the whole test case
        cls.user1 = IouUser.objects.create(name="Tony")
        cls.user2 = IouUser.objects.create(name="Peter")
        cls.user3 = IouUser.objects.create(name="Bruce")

    def test_iou_create(self):
        """
        Ensure we can create a new entry for iou.
        """
        url = reverse('ledger-list')
        data = {"user": IouTests.user1.id, "owes": IouTests.user2.id, "amount": 100, "expiration": "2022-11-25 00:00:00"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ledger.objects.count(), 1)
        self.assertEqual(Ledger.objects.get().user.name, 'Tony')
        self.assertEqual(Ledger.objects.get().owes.name, 'Peter')
        self.assertEqual(Ledger.objects.get().amount, 100)
        self.assertEqual(Ledger.objects.get().expiration, datetime(2022, 11, 25, 0, 0, tzinfo=timezone.utc))

    def test_iou_self_owe(self):
        """
        Ensure that a person cannot create an entry owing money to himself
        """
        url = reverse('ledger-list')
        data = {"user": IouTests.user1.id, "owes": IouTests.user1.id, "amount": 100, "expiration": "2022-11-25 00:00:00"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_iou_negative_amount(self):
        """
        Ensure that a person cannot enter a negative amount
        """
        url = reverse('ledger-list')
        data = {"user": IouTests.user3.id, "owes": IouTests.user2.id, "amount": -100, "expiration": "2022-11-25 00:00:00"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_iou_amount_is_zero(self):
        """
        Ensure that a person cannot enter a negative amount
        """
        url = reverse('ledger-list')
        data = {"user": IouTests.user3.id, "owes": IouTests.user2.id, "amount": 0, "expiration": "2022-11-25 00:00:00"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
