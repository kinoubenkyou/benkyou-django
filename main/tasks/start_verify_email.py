from secrets import token_urlsafe

from celery import shared_task
from django.core.cache import cache
from django.core.mail import send_mail
from django.utils.http import urlencode

from main.models import User


@shared_task
def start_verify_email(server_url, user_id):
    token = token_urlsafe()
    cache.set(f"verify_email.{user_id}", token)
    send_mail(
        "Verify Email",
        f"{server_url}/user/verify_email/?{urlencode({"token": token})}",
        None,
        [User.objects.get(id=user_id).email],
    )
