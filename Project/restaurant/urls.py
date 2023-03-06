from django.urls import path
import restaurant.views as v


urlpatterns = [
    path('', v.home, name="home"),
    path('sign_up', v.sign_up, name=""),
]
