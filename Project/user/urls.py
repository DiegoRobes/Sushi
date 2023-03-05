from django.urls import path
import user.views as v

urlpatterns = [
    path('register/', v.register, name="register"),
]
