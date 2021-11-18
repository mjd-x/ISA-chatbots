from django.test import Client, TestCase
from chat.models import Person, Bot, Chat


class RegisterTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        response = self.client.post("/register/", {"username": "logintest", "password": "somepassword", "email": "login@test.com"})
        self.assertEqual(response.status_code, 302)

class StartChatApiTest(TestCase):
    fixtures = ['seed.json']

    def setUp(self):
        self.client = Client()

    def test_details(self):
        response = self.client.post("/api/start-chat/", {"name": "someuser", "message": "this is a test"})
        self.assertEqual(response.status_code, 201)

        id = response.json()['uri']
        uri = "/api/chats/" + str(id[-1])

        self.assertEqual(uri, "/api/chats/1")

class LoginTest(TestCase):
    fixtures = ['seed.json']

    def setUp(self):
        Person.objects.create_user(username="someuser", password="somepassword", email="some@email.com", is_active=True)
        self.client = Client()

    def test_details(self):
        response = self.client.post("/", {"name": "someuser", "password": "somepassword"})
        self.assertEqual(response.status_code, 200)