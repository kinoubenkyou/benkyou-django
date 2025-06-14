from typing import TYPE_CHECKING, Any

from django.core.cache import cache
from django.http import HttpResponse
from django.views.generic import FormView
from rest_framework.reverse import reverse_lazy

from main.forms.user.reset_password import UserResetPasswordForm
from main.models import User

if TYPE_CHECKING:
    FormView_ = FormView[UserResetPasswordForm]  # pragma: no cover
else:
    FormView_ = FormView


class UserResetPasswordView(FormView_):
    form_class = UserResetPasswordForm
    success_url = reverse_lazy("user-sign-in")
    template_name = "form.html"

    def form_valid(self, form: UserResetPasswordForm) -> HttpResponse:
        """Set user password, delete token from cache."""
        user = User.objects.get(username=form.cleaned_data["username"])
        user.set_password(form.cleaned_data["password"])
        user.save()
        cache.delete(f"reset_user_email.{form.cleaned_data['username']}")
        return super().form_valid(form)

    def get_initial(self) -> dict[str, Any]:
        """Set initial token value, username value from query string."""
        initial = super().get_initial()
        initial["token"] = self.request.GET.get("token")
        initial["username"] = self.request.GET.get("username")
        return initial
