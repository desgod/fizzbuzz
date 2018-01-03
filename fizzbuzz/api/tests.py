from datetime import datetime, timezone
from unittest import mock

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from fizzbuzz.api.models import FizzBuzz


TEST_TIME = datetime.now(timezone.utc)


class FizzBuzzTests(APITestCase):

    def setUp(self):
        with mock.patch('django.utils.timezone.now') as mock_now:  # mock time for creation_date field
            mock_now.return_value = TEST_TIME
            FizzBuzz.objects.create(message="Hello World", useragent="unittest")

    def test_post_fizzbuzz(self):
        """
        Testing POST endpoint 
        """

        url = reverse('fizzbuzz-list')
        data = {"message": "Test post"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FizzBuzz.objects.count(), 2)

    def test_get_fizzbuzz_list(self):
        """
        Ensure we can get a list of fizzbuzz's
        """

        url = reverse('fizzbuzz-list')
        response = self.client.get(url)
        response.render()

        self.assertEqual(len(response.data), 1)

    def test_get_fizzbuzz_by_id(self):
        """
        Testing GET of FizzBuzz by ID 
        """
        response = self.client.get('/fizzbuzz/1/')
        response.render()

        self.assertEqual(response.data, {"message": "Hello World",
                                         "useragent": "unittest",
                                         "creation_date": str(TEST_TIME.isoformat()).replace('+00:00', 'Z'),
                                         "fizzbuzz_id": 1})

    def test_get_fizzbuzz_by_id_doesnt_exist(self):
        """
        Testing GET of FizzBuzz by ID where the ID doesn't exist
        """
        response = self.client.get('/fizzbuzz/2/')
        response.render()

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

