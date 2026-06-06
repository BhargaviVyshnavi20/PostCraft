from django.shortcuts import render, get_object_or_404
from django.db.models import Q
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




def post_details(request, slug):
    post = get_object_or_404(Blog, slug=slug, status=1)
    return render(request, 'post.html', {'post': post})


def search(request):
    keyword = request.GET.get('keyword', '').strip()
    if keyword:
        posts = Blog.objects.filter(
            Q(title__icontains=keyword) |
            Q(description__icontains=keyword) |
            Q(content__icontains=keyword),
            status=1
        ).order_by('-created_at')
    else:
        posts = Blog.objects.none()
    
    context = {
        'posts': posts,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)