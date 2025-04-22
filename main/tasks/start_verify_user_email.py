from secrets import token_urlsafe
from typing import Any
from urllib.parse import urlunparse

from celery import shared_task
from django.core.cache import cache
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.http import urlencode

from main.models import User


@shared_task  # type: ignore[misc]
def start_verify_user_email(netloc: str, scheme: str, user_id: Any) -> None:
    """Set token to verify user email in cache."""
    token = token_urlsafe()
    cache.set(f"verify_user_email.{user_id}", token, 600)
    send_mail(
        "Verify Email",
        urlunparse(
            [
                scheme,
                netloc,
                reverse("user-verify-email"),
                None,
                urlencode({"token": token}),
                None,
            ],
        ),
        None,
        [User.objects.get(pk=user_id).email],
    )
