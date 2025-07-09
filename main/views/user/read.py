from main.views.read import ReadView
from main.views.user.user_object_mixin import UserObjectMixin


class UserReadView(UserObjectMixin, ReadView):
    object_fields = (
        "username",
        "email",
        "email_is_verified",
    )
