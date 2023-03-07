from django.urls import path
import cart.views as v

urlpatterns = [
    path('', v.empty_cart, name="cart"),
]
