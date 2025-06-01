from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


class UserUpdatePasswordView(PasswordChangeView):
    success_url = reverse_lazy("user-read")
    template_name = "form.html"
