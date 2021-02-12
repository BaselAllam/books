from django.urls import path
from cart import views


urlpatterns = [
    path('carts/<int:userId>/', views.cart, name='carts'),
    path('carts/<int:userId>/<int:bookId>/', views.buy, name='buy'),
]
