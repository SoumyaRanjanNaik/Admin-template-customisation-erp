from django.db import models
from django.conf import settings


# Create your models here.
class Request(models.Model):
    """Model definition for Request."""

    request_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                                  related_name="user")
    location = models.CharField(blank=True, null=True, max_length=150)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                                    related_name="assigned_to")
    assigned_date = models.DateTimeField(null=True, blank=True, auto_now=True)
    status = models.CharField(
        null=True,
        blank=True,
        max_length=10,
        choices=[
            ("Assigned", "Assigned"),
            ("Requested", "Requested"),
            ("Cancelled", "Cancelled"),
            ("Rejected", "Rejected"),
            ("Completed", "Completed"),
            ],
        default="Requested",
        )

    class Meta:
        """Meta definition for Request."""

        verbose_name = "Request"
        verbose_name_plural = "Requests"

    def __str__(self):
        """Unicode representation of Request."""
        return str(self.user_name)


class UserDetail(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(null=True, blank=True, verbose_name='Name', max_length=50)
    contact = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "User Detail"
        verbose_name_plural = "User Details"

    def __str__(self):
        return self.user.username
