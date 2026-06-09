from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blogs.models import Category, Blog

class BlogSearchTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.category = Category.objects.create(category_name='Technology')
        self.published_blog = Blog.objects.create(
            title='Django Search Tutorial',
            slug='django-search-tutorial',
            category=self.category,
            author=self.user,
            description='Learn how to build a search feature in Django',
            content='Search content here',
            status=1,
            is_featured=False
        )
        self.draft_blog = Blog.objects.create(
            title='Draft Search Tutorial',
            slug='draft-search-tutorial',
            category=self.category,
            author=self.user,
            description='Learn how to build a search feature in Django (Draft)',
            content='Search content here',
            status=0,
            is_featured=False
        )

    def test_search_results_matching(self):
        url = reverse('search')
        response = self.client.get(url, {'keyword': 'Django'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Django Search Tutorial')
        self.assertNotContains(response, 'Draft Search Tutorial')

    def test_search_results_no_keyword(self):
        url = reverse('search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No articles matched your search query')


class UserRegistrationTestCase(TestCase):
    def test_registration_page_get(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
        self.assertContains(response, 'Create Account')

    def test_registration_successful_post(self):
        url = reverse('register')
        data = {
            'username': 'newuser',
            'first_name': 'New',
            'last_name': 'User',
            'email': 'newuser@example.com',
            'password1': 'StrongPassword123!',
            'password2': 'StrongPassword123!',
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('home'))
        
        # Verify user is created in database
        self.assertTrue(User.objects.filter(username='newuser').exists())
        user = User.objects.get(username='newuser')
        self.assertEqual(user.first_name, 'New')
        self.assertEqual(user.last_name, 'User')
        self.assertEqual(user.email, 'newuser@example.com')
        
        # Verify user is logged in
        self.assertEqual(int(self.client.session['_auth_user_id']), user.pk)

    def test_registration_invalid_post_mismatch_password(self):
        url = reverse('register')
        data = {
            'username': 'newuser',
            'first_name': 'New',
            'last_name': 'User',
            'email': 'newuser@example.com',
            'password1': 'StrongPassword123!',
            'password2': 'DifferentPassword123!',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='newuser').exists())
        self.assertContains(response, "The two password fields")


class UserLoginLogoutTestCase(TestCase):
    def setUp(self):
        self.username = 'loginuser'
        self.password = 'TestPassword123!'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
            email='login@example.com'
        )

    def test_login_page_get(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, 'Sign In')

    def test_login_successful_post(self):
        url = reverse('login')
        data = {
            'username': self.username,
            'password': self.password,
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('home'))
        
        # Verify user is logged in
        self.assertEqual(int(self.client.session['_auth_user_id']), self.user.pk)

    def test_login_invalid_post(self):
        url = reverse('login')
        data = {
            'username': self.username,
            'password': 'wrongpassword',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a correct username and password')

    def test_logout_post(self):
        # Log in first
        self.client.login(username=self.username, password=self.password)
        
        # Logout POST
        url = reverse('logout')
        response = self.client.post(url)
        self.assertRedirects(response, reverse('home'))
        
        # Verify user is logged out
        self.assertNotIn('_auth_user_id', self.client.session)


