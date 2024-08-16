from django.test import Client, TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from todolist.models import CustomUser, TodoItem


class TodoListTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='test_user', password='test_user')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_todolist_get(self):
        response = self.client.get('/todos/')
        self.assertEqual(response.status_code, 200)
        
    def test_todolist_post(self):
        data = {
            "title": "New Task",
            "description": "Test description",
            "tags": "blue",
            "taskType": "todo",
            "author": self.user.id
        }
        post_response = self.client.post('/todos/', data, format='json')
        self.assertEqual(post_response.status_code, 201)
        
    def test_todolist_put(self):
        todo = TodoItem.objects.create(
            title="Old Task", 
            description="Old description", 
            tags="blue", 
            taskType="todo", 
            author=self.user
        )
                
        update_data = {
            "title": "Updated Task",
            "description": "Updated description",
            "tags": "green",
            "taskType": "inProgress",
            "author": self.user.id
        }
        # todo_id = post_response.data['id'] 
        put_response = self.client.put(f'/todos/{todo.id}/', update_data, format='json')
        self.assertEqual(put_response.status_code, 200)
        
    def test_todolist_patch(self):
        todo = TodoItem.objects.create(
            title="Partially Updated Task", 
            description="Old description", 
            tags="blue", 
            taskType="todo", 
            author=self.user
        )

        patch_data = {
            "title": "Patched Task Title"
        }
        patch_response = self.client.patch(f'/todos/{todo.id}/', patch_data, format='json')
        self.assertEqual(patch_response.status_code, 200)
        
    def test_todolist_delete(self):
        
        todo = TodoItem.objects.create(
            title="Task to be deleted", 
            description="This task will be deleted", 
            tags="blue", 
            taskType="todo", 
            author=self.user
    )
        delete_response = self.client.delete(f'/todos/{todo.id}/')
        self.assertEqual(delete_response.status_code, 200)
        

        
class TestUserRegister(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.first_name = 'TestFirstNane'
        self.last_name = 'TestLastName'
        self.username = 'testuser'
        self.email = 'testuser@email.com'
        self.password = 'password'

        
    def test_signup(self):
        response = self.client.post('/register/', {
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
                