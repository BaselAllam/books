from django.http.response import HttpResponse
from django.shortcuts import render
from cart.models import Cart


def cart(request, userId):
    try:
        carts = Cart.objects.filter(user = userId)
        return render(request, 'all_carts.html', {'carts' : carts})
    except Cart.DoesNotExist:
        return HttpResponse('no item found')





def buy(request, userId, bookId):
    try:
        carts = Cart.objects.filter(user = userId, book = bookId)
        carts.bought = True
        carts.save()
        return render(request, 'all_carts.html', {'carts' : carts})
    except:
        return HttpResponse('some thing went wrong')