from django.shortcuts import render
from blogs.models import Category, Blog 


def home(request):
    categories = Category.objects.all()
    featured_blogs = Blog.objects.filter(is_featured=True).order_by('-created_at')
    posts = Blog.objects.filter(is_featured=False, status=1).order_by('-created_at')

    print(featured_blogs)
    context = {
        'categories' : categories,
        'featured_blogs' : featured_blogs,
        'posts': posts,
    }
    return render(request, 'home.html', context)