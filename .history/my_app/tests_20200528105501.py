from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class CraiglistCloneTestCase(TestCase):

    def setUp(self):
        self.search = self.post.get('search')
        print(self.search)

    def test_homepage(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed('base.html')

    # def test_searchpage(self):
    #     res = self.client.post(reverse('new_search'))
        # self.assertEqual(res.status_code, 200)
        # self.assertTemplateUsed('my_app/new_search.html')
