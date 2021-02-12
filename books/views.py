from book.models import Book
from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    books = Book.objects.all()[:2]
    context = {
        'books' : books
    }
    return render(request, 'home.html', context)





def about(request):
    return render(request, 'about.html')