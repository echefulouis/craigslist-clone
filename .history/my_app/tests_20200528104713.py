from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class CraiglistCloneTestCase(TestCase):

    def test_server_up(self):
        res = self.client.get(reverse('home'))
        # print(res)
        # self.assertEqual(res.status_code, 200)
