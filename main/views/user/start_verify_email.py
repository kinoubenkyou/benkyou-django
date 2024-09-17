from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView

from main.forms.user import UserStartVerifyEmailForm
from main.tasks import start_verify_email


class UserStartVerifyEmailView(LoginRequiredMixin, FormView):
    form_class = UserStartVerifyEmailForm
    success_url = "/user/"
    template_name = "main/user/start_verify_email.html"

    def form_valid(self, form):
        return_ = super().form_valid(form)
        start_verify_email.delay(
            self.request.get_host(),
            self.request.scheme,
            self.request.user.id,
        )
        return return_
