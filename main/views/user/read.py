from django.contrib.auth.mixins import LoginRequiredMixin

from main.views import ReadView


class UserReadView(LoginRequiredMixin, ReadView):
    field_names = (
        "last_login",
        "username",
        "first_name",
        "last_name",
        "email",
        "date_joined",
    )

    def get_object(self, queryset=None):  # type: ignore[no-untyped-def]
        """Override the object with the authenticated user."""
        return self.request.user
