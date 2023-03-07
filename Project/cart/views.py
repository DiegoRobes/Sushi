from django.shortcuts import render


# Create your views here.
def cart(request):
    context = {"items": False}
    return render(request, 'cart/cart.html', context=context)


