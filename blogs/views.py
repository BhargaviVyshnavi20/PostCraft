from django.shortcuts import render, get_object_or_404
from .models import Blog, Category

def post_by_category(request, category_id):
    posts = Blog.objects.filter(category_id=category_id, status=1)
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        return render(request, '404.html')
    context = {
        'posts': posts,
        'Category': category,
    }
    return render(request, 'posts_by_category.html', context)
