from django.shortcuts import render


# Create your views here.
def empty_cart(request):
    context = {"items": True}
    return render(request, 'cart/cart.html', context=context)


