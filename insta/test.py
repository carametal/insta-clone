from django.test import TestCase, Client
from django.contrib.auth.models import User
from insta.models import Post
from io import StringIO

DAMMY_IMAGE =  StringIO(
    'GIF87a\x01\x00\x01\x00\x80\x01\x00\x00\x00\x00ccc,\x00'
    '\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;'
)
DAMMY_CAPTION = 'It is test caption.'
DAMMY_USERNAME = 'testuser'


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

class PostTest(TestCase):

    def test_post(self):
        params = {
            'image': DAMMY_IMAGE,
            'caption': DAMMY_CAPTION
        }
        client = Client()
        client.force_login(User.objects.create_user(DAMMY_USERNAME))
        response = client.post('/post/', params)
        post = Post.objects.get(id=1)
        self.assertEquals(post.user_id.username, DAMMY_USERNAME)
