from django.urls import path

from two import views

urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path("generate_request/", views.generate_request, name="generate_request"),
    path("view_requests/", views.view_requests, name="view_requests"),
    path("view_requests/<msg>", views.view_requests, name="view_requests"),
]
