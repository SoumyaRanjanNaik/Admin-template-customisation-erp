from django.contrib import admin
from django.utils.html import format_html

from one.models import Request


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    """Admin View for Request"""

    user_is = None

    def get_list(self, request):
        if request.user.is_superuser:
            user_is = "u"

    if user_is == "u":
        search_fields = (
            "user_name",
            "location",
            "request_date",
            "assigned_date",
            "assigned_to",
        )

        list_display = (
            "user_name",
            "location",
            "request_date",
            "assigned_date",
            "assigned_to",
            "current_status",
        )
        list_filter = (
            "request_date",
            "assigned_date",
            "status",
        )
        readonly_fields = ("request_date", "assigned_date")
        date_hierarchy = "assigned_date"
        autocomplete_fields = ("assigned_to",)
    else:
        search_fields = (
            "user_name",
            "location",
            "request_date",
            "assigned_date",
        )

        list_display = (
            "user_name",
            "location",
            "request_date",
            "assigned_date",
            "current_status",
        )
        list_filter = (
            "request_date",
            "assigned_date",
            "status",
        )
        readonly_fields = (
            "request_date",
            "assigned_date",
            "user_name",
            "location",
            "assigned_to",
        )
        date_hierarchy = "assigned_date"

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            queryset = queryset
        else:
            queryset = queryset.filter(assigned_to=request.user)

        return queryset

    def current_status(self, obj):
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
