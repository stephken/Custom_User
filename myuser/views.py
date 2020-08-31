from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from myuser.forms import SignupForm, LoginForm
from myuser.models import MyUser
from custom_users.settings import AUTH_USER_MODEL
from django.contrib.auth.decorators import login_required


# Create your views here.

def index_view(request):
    return render(
        request, "index.html",
        {"welcome": "this to under the scope by Ken: Custom Users assessment", "AUTH_USER_MODEL": AUTH_USER_MODEL},
    )


def signup_view(request):
    if request.method == "POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = MyUser.objects.create_user(
                password=data.get("password"),
                username=data.get("username"),
                age=data.get("age"),
                display_name=data.get("display_name"),
                homepage=data.get("homepage"),
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse("home"))

    form = SignupForm()
    return render(request, "generic_form.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=authenticate(
                request, username=data.get("username"), password=data.get("password")
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("home"))

        form = LoginForm()
        return render(request, "generic_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))
