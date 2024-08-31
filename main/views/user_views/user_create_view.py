from django.contrib.auth.models import User
from django.views.generic import CreateView

from main.forms.user_forms import UserCreateForm
from main.tasks import start_verify_email


class UserCreateView(CreateView):
    form_class = UserCreateForm
    model = User
    success_url = "/user/create_done/"
    template_name = "main/user/create.html"

    def form_valid(self, form):
        result = super().form_valid(form)
        start_verify_email.delay(
            f"{self.request.scheme}://{self.request.get_host()}", self.object.id
        )
        return result
