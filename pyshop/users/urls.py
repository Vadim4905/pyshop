from django.urls import path

from .views import RegisterView, user_exit,ShopLoginView,SendEmail

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"), 
    path("logout/", user_exit, name="logout"),  
    path("login/", ShopLoginView.as_view(), name="login"), 
    path("send/", SendEmail.as_view(), name="send"), 

]