from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': dashboard})


# custom log-in view
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd["username"], password=cd["password"])
            if user is None:
                return HttpResponse("Disabled login")
            login(request, user)
            return HttpResponse("Authenticated successfully")
    else:
        form = LoginForm()
        return render(request, "account/login.html", {"form": form})
