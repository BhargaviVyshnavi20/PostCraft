from .models import Category, About

def get_categories(request):
    categories = Category.objects.all()
    about = About.objects.first()
    return {
        'categories': categories,
        'about': about,
    }