from django.urls import path

from .views import RegisterView, user_exit

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"), 
    path("logout/", user_exit, name="logout"),  
]