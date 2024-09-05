from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class UserStartVerifyEmailDoneView(LoginRequiredMixin, TemplateView):
    template_name = "main/user/start_verify_email_done.html"
