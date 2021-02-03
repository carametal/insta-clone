from django.test import TestCase, Client
from django.contrib.auth.models import User

class UsersTest(TestCase):

    def test_signup(self):
        client = Client()
        params = {
            'username': 'john',
            'email': 'john@example.com',
            'password': 'smith',
            'confirm_password': 'smith'
        }
        response = client.post('/session_signup/', params)
        user = User.objects.get(username='john')
        self.assertEqual(user.username, 'john')
        self.assertEqual(user.email, 'john@example.com')

