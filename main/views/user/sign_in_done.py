from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class UserSignInDoneView(LoginRequiredMixin, TemplateView):
    template_name = "main/user/sign_in_done.html"
