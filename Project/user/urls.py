from django.urls import path
import user.views as v

urlpatterns = [
    path('welcome/', v.welcome, name="welcome"),
    path('login/', v.login, name="login"),
    path('sign_up/', v.sign_up, name="sign_up"),
    path('my_account/', v.my_account, name="my_account"),
]
