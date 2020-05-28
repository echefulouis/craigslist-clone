from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class CraiglistCloneTestCase(TestCase):

    def setUp(self):
        self.search_item = {'search': 'Muffin'}
        print(self.search_item)

    def test_homepage(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed('base.html')

    def test_searchpage(self):
        # , content_type='application/json')
        res = self.client.post(reverse('new_search'), data=self.search_item)
        # self.assertEqual(res.status_code, 200)
        # self.assertTemplateUsed('my_app/new_search.html')
