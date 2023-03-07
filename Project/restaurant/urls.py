from django.urls import path
import restaurant.views as v


urlpatterns = [
    path('', v.home, name="home"),
    path('/about', v.about, name="about"),

]
