from django.http import HttpResponse
from book.models import Book
from django.shortcuts import render



def first_view(request):
    books = Book.objects.all()
    return HttpResponse(books)



def search(request, bookName):
    try:
        book = Book.objects.get(bookName = bookName)
        return HttpResponse('the book you searched about is {}'.format(book))
    except:
        return HttpResponse('no book found')