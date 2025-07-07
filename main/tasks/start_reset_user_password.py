from secrets import token_urlsafe
from urllib.parse import urlunparse

from celery import shared_task
from django.core.cache import cache
from django.core.mail import send_mail
from django.utils.http import urlencode

from main.models import User


@shared_task  # type: ignore[misc]
def start_reset_user_password(netloc: str, scheme: str, username: str) -> None:
    """Set token to reset user password in cache, send email."""
    token = token_urlsafe()
    cache.set(f"reset_user_password.{username}", token)
    send_mail(
        "Reset Password",
        urlunparse(
            [
                scheme,
                netloc,
                "/user/reset_password",
                None,
                urlencode({"token": token, "username": username}),
                None,
            ],
        ),
        None,
        [User.objects.get(username=username).email],
    )
