from django.contrib.auth.mixins import LoginRequiredMixin

from main.views import ReadView


class UserReadView(LoginRequiredMixin, ReadView):
    excluded_fields = ("id", "is_active", "is_staff", "is_superuser", "password")

    def get_object(self, _queryset=None):
        return self.request.user
