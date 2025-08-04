from django.contrib import admin
from .models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    search_fields = ['name',]
    list_filter = ['created_at',]


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at', 'viewscount', 'category']
    search_fields = ['title', 'content']
    list_filter = ['created_at', 'updated_at', 'category']

    
admin.site.register(Article, ArticleAdmin)

admin.site.register(Category, CategoryAdmin)