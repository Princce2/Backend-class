from django.urls import path
from .views import index, detail, categories

urlpatterns = [
    path('/<int:category_id>/', index, name='index'),
    path('article/<int:id>/', detail, name='detail'),
    path('categories/', categories, name="Category")
]
