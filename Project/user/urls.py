from django.urls import path
import user.views as v

urlpatterns = [
    path('sign_up/', v.sign_up, name="sign_up"),
]
