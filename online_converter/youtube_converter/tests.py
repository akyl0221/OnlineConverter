from django.test import TestCase
from django.urls import reverse


class Tester(TestCase):

    def setUp(self):
        self.valid_url = 'https://www.youtube.com/watch?v=afvFJpo30bQ'

    def test_valid_form(self):
        url = reverse('converter')

        load = {
            'url': self.valid_url
        }

        test = self.client.post(url, load)

        self.assertEqual(test.status_code, 301)

    def test_get_request(self):
        url = reverse('converter')

        test = self.client.get(url)

        self.assertEqual(test.status_code, 200)

    def test_invalid_form(self):
        url = reverse('converter')

        test = self.client.post(url)

        self.assertEqual(test.status_code, 200)

