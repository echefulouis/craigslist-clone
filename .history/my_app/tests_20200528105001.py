from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class CraiglistCloneTestCase(TestCase):

    def test_homepage(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)
        print(dir(self))

    # def test_searchpage(self):
    #     res = self.client.get(reverse(''))
