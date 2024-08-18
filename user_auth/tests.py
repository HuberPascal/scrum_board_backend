from django.test import Client, TestCase
from rest_framework.test import APIClient
from todolist.models import CustomUser, TodoItem


# Create your tests here.
class TestUserRegister(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.first_name = 'TestFirstNane'
        self.last_name = 'TestLastName'
        self.username = 'testuser'
        self.email = 'testuser@email.com'
        self.password = 'password'

        
    def test_signup(self):
        response = self.client.post('/auth/register/', {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'email': self.email,
            'password': self.password,
        }, format='json')
        
        self.assertEqual(response.status_code, 201)

    def test_signin(self):
        user = CustomUser.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        
        c = Client()
        logged_in = c.login(username='testuser', password='12345')