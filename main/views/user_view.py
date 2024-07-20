from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from main.forms import UserCreateForm, UserUpdateForm
from main.models import User


class UserCreateView(CreateView):
    form_class = UserCreateForm
    model = User
    template_name_suffix = "_create_form"


class UserDeleteView(DeleteView):
    model = User

    def get_success_url(self):
        return reverse("user-list")


class UserDetailView(DetailView):
    model = User


class UserListView(ListView):
    model = User


class UserUpdateView(UpdateView):
    form_class = UserUpdateForm
    model = User
    template_name_suffix = "_update_form"
