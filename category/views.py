from django.http.response import HttpResponse
from django.shortcuts import render
from category.models import Category
from book.models import Book


def all_category(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories
    }
    return render(request, 'all_categories.html', context)





def category_books(request, id):
    try:
        books = Book.objects.filter(category = id)
        category = Category.objects.get(categoryId = id)
        context = {
            'category_books' : books,
            'id' : category.categoryName,
        }
        return render(request, 'category_books.html', context)
    except:
        return HttpResponse('no result found')