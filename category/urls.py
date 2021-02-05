from django.urls import path
from category import views


urlpatterns = [
    path('allcategories/', views.all_category),
    path('categorybooks/<int:id>', views.category_books)
]
