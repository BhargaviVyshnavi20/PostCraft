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

