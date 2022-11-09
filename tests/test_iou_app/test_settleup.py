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

        cls.ldg1 = Ledger.objects.create(user=cls.user1,owes=cls.user2,amount=100,expiration="2022-11-25 00:00:00+0000")


    def test_settleup(self):
        """
        Ensure that the list of users we get are accurate
        """
        url = '/settleup/'
        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),2)
        self.assertEqual(response.data[0]["name"],"Peter")
        self.assertEqual(response.data[1]["name"],"Tony")
        



