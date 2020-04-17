from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db import IntegrityError
from one.models import UserDetail


def home(request):
    if request.user.is_authenticated:
        return redirect("profile")
    else:
        return render(request, "base.html")


def register(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        contact = request.POST.get("contact")
        try:
            user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
            user_detail = UserDetail(user=user, name=name, contact=contact)
            user_detail.save()
            login(request, user=user)
            return redirect("profile")
        except IntegrityError:
            context["message"] = "Already registered"
            return render(request, "sign_up.html", context)
    else:
        return render(request, "sign_up.html")
