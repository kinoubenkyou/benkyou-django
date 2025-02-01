from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.views.generic.edit import DeleteView

from main.models import User


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User  # type: ignore[assignment]
    success_url = reverse_lazy("user-sign-in")
    template_name = "form.html"  # type: ignore[assignment]

    def get_object(self, queryset=None):  # type: ignore[no-untyped-def]
        """Override the object with the authenticated user."""
        return self.request.user
