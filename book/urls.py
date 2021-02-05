from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('books/', views.first_view),
    path('search/<int:id>/', views.search)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
