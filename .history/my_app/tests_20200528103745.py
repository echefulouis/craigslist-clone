from django.test import TestCase

# Create your tests here.


class CraiglistCloneTestCase(TestCase):

    def test_server_up(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
