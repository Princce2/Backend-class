from django.shortcuts import render, get_object_or_404
from .models import Article, Category


"""
ModelName.objects.all() --> all data
ModelName.objects.filter(user=user) --> filter by user
get_object_or_404(Article, id=article_id) --> get object or 404
ModelName.objects.filter(user=user).first() --> get first object
"""

def index(request, category_id=None):
    articles = Article.objects.all()
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(category=category)
    return render(request, 'index.html', {'articles': articles, "categories": categories, 'articles': articles})


def detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'index.html', {'article': article})

def categories(request):
    categories = Category.objects.all()
    print(categories)
    return render(request, 'base.html', {"categories": categories})
