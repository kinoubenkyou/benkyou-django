from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.views.generic.edit import UpdateView

from main.models import User


class UserUpdateView(LoginRequiredMixin, UpdateView):
    fields = ("username", "first_name", "last_name", "email")  # type: ignore[assignment]
    model = User  # type: ignore[assignment]
    success_url = reverse_lazy("user-read")
    template_name = "form.html"  # type: ignore[assignment]

    def get_object(self, queryset=None):  # type: ignore[no-untyped-def]
        return self.request.user
