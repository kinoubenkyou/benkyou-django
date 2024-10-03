from django.forms import EmailField

from main.models import User


class UserEmailField(EmailField):
    def clean(self, value):
        if not value:
            return None
        user = User.objects.filter(email=super().clean(value)).first()
        if not user:
            return -1
        return user.id
