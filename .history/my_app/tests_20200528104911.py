from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class CraiglistCloneTestCase(TestCase):

    def test_server(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)
