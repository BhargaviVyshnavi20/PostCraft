from django.contrib import admin
from .models import Category, Blog

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    list_editable = ('status', 'is_featured')
    list_filter = ('status', 'is_featured', 'category__category_name', 'author__username')
    search_fields = ('id','title', 'category__category_name', 'author__username')
    ordering = ('-created_at',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
