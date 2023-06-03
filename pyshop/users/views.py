from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

class RegisterView(CreateView):
    template_name = "users/register.html"
    form_class = UserCreationForm
    
    def form_valid(self, form: UserCreationForm):
        user = form.save()
        login(self.request, user)
        return redirect("/")

def user_exit(request):
    logout(request)
    return redirect("/")

    
#tratatata333 1 user
#tratatata334 2 user
#tratatata335 3 user