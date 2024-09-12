from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView


class UserReadView(LoginRequiredMixin, DetailView):
    template_name = "main/user/read.html"

    def get_object(self, _queryset=None):
        return self.request.user
