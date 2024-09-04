from secrets import token_urlsafe
from urllib.parse import urlunparse

from celery import shared_task
from django.core.cache import cache
from django.core.mail import send_mail
from django.utils.http import urlencode

from main.models import User


@shared_task
def start_verify_email(netloc, scheme, user_id):
    token = token_urlsafe()
    cache.set(f"verify_email.{user_id}", token)
    send_mail(
        "Verify Email",
        urlunparse(
            [
                scheme,
                netloc,
                "/user/verify_email",
                None,
                urlencode({"token": token}),
                None,
            ]
        ),
        None,
        [User.objects.get(id=user_id).email],
    )
