from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import UpdateView

from main.forms.user import UserUpdateForm


class UserUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    model = User
    success_url = "/user/"
    template_name = "main/user/update.html"

    def get_object(self, _queryset=None):
        return self.request.user
