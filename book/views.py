from django.http import HttpResponse
from book.models import Book
from django.shortcuts import render


def first_view(request):
    books = Book.objects.all()
    context = {
        'books' : books
    }
    return render(request, 'all_books.html', context)
    #return HttpResponse(books)



def search(request, id):
    try:
        book = Book.objects.get(id = id)
        context = {
            'book' : book
        }
        return render(request, 'search_book.html', context)
        #return HttpResponse('the book you searched about is {}'.format(book))
    except:
        return HttpResponse('no book found')