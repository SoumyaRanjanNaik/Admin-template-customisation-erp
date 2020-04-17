from django.contrib import admin
from django.db import models
from django.forms.widgets import NumberInput
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from one.models import Request, UserDetail
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    """Admin View for Request"""

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if request.user.is_superuser:
            self.search_fields = (
                "user_name",
                "location",
                "request_date",
                "assigned_date",
                "assigned_to",
                )
            self.list_display = (
                "user_name",
                "location",
                "request_date",
                "assigned_date",
                "assigned_to",
                "current_status",
                )
            self.list_filter = (
                "request_date",
                "assigned_date",
                "status",
                )
            self.readonly_fields = ("request_date", "assigned_date")
            self.date_hierarchy = "assigned_date"
            self.autocomplete_fields = ("assigned_to",)
        else:
            self.search_fields = (
                "user_name",
                "location",
                "request_date",
                "assigned_date",
                )
            self.list_display = (
                "user_name",
                "location",
                "request_date",
                "assigned_date",
                "current_status",
                )
            self.list_filter = (
                "request_date",
                "assigned_date",
                "status",
                )
            self.readonly_fields = (
                "request_date",
                "assigned_date",
                "user_name",
                "location",
                "assigned_to",
                )
            self.date_hierarchy = "assigned_date"
        return super().change_view(request, object_id, extra_context=extra_context)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            queryset = queryset
        else:
            queryset = queryset.filter(assigned_to=request.user)

        return queryset

    @staticmethod
    def current_status(obj):
        if obj.status == "Assigned":
            return format_html('<button class="buttonAss">Assigned</button>')
        elif obj.status == "Requested":
            return format_html('<button class="buttonReq">Requested</button>')
        elif obj.status == "Cancelled":
            return format_html('<button class="buttonCan">Cancelled</button>')
        elif obj.status == "Rejected":
            return format_html('<button class="buttonRej">Rejected</button>')
        elif obj.status == "Completed":
            return format_html('<button class="buttonCom">Completed</button>')

    class Media:
        css = {"all": ("css/admin.css",)}


# admin.site.unregister(User)


@admin.register(UserDetail)
class CustomUserAdmin(admin.ModelAdmin):
    """
        Admin View for Users
    """
    fields = ("user", "name", "contact")
    autocomplete_fields = ["user"]

    formfield_overrides = {
        models.IntegerField: {"widget": NumberInput(attrs={"size": "20"})},
        }
