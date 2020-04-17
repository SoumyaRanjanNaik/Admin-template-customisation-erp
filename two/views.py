from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from one.models import Request
import json


def profile(request):
    return render(request, "profile_home.html")


def generate_request(request):
    if request.method == "POST":
        location = request.POST.get("location")
        user = request.user
        request = Request(user_name=user, location=location)
        request.save()
        return redirect("view_requests", msg="your Request has been saved")
    else:
        return render(request, "generate_request.html")


def view_requests(request, msg=None):
    if msg is not None:
        context = {"msg": msg}
    else:
        context = {}
    req = Request.objects.all().order_by("-id")
    p = Paginator(req, 10)
    page_number = request.GET.get("page")
    page_obj = p.get_page(page_number)
    context["page_obj"] = page_obj
    return render(request, "view_requests.html", context)
