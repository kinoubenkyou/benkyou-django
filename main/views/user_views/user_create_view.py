from django.contrib.auth.models import User
from django.views.generic import CreateView

from main.forms.user_forms import UserCreateForm


class UserCreateView(CreateView):
    form_class = UserCreateForm
    model = User
    success_url = "/user/create_done/"
    template_name = "main/user/create.html"
