from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import BookListView, AddBook

urlpatterns = [
    path('books/', views.first_view),
    path('search/<int:id>/', views.search),
    path('bookListView/', BookListView.as_view()),
    path('bookDetails/<int:id>/', views.search, name='book_details'),
    path('addBook/', AddBook.as_view(), name='add_book')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
