from django.http import HttpResponse
from book.models import Book
from django.shortcuts import render
from django.views.generic import ListView, CreateView

def first_view(request):
    books = Book.objects.all()
    context = {
        'books' : books
    }
    return render(request, 'all_books.html', context)
    #return HttpResponse(books)



class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    ordering = ['publishedDate']
    template_name = 'all_books.html'



def search(request, id):
    try:
        book = Book.objects.get(id = id)
        context = {
            'book' : book
        }
        return render(request, 'book_details.html', context)
        #return HttpResponse('the book you searched about is {}'.format(book))
    except:
        return HttpResponse('no book found')






class AddBook(CreateView):
    model = Book
    fields = ['bookName', 'bookPrice', 'bookDescription', 'category']
    template_name = 'add_book.html'