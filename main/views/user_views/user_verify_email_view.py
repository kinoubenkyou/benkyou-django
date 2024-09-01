from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.core.exceptions import BadRequest
from django.views.generic import FormView

from main.forms.user_forms import UserVerifyEmailForm


class UserVerifyEmailView(LoginRequiredMixin, FormView):
    form_class = UserVerifyEmailForm
    success_url = "/user/"
    template_name = "main/user/verify_email.html"

    def form_valid(self, form):
        cache_key = f"verify_email.{self.request.user.id}"
        token = cache.get(cache_key, object())
        if token != form.cleaned_data["token"]:
            raise BadRequest("Token doesn't match.")
        user = self.request.user
        user.email_verified = True
        user.save()
        if not cache.delete(cache_key):
            raise Exception("Couldn't delete token.")
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        initial["token"] = self.request.GET.get("token")
        return initial
