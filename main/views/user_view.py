from django.views.generic import CreateView, DetailView, ListView, UpdateView

from main.forms import UserCreateForm, UserUpdateForm
from main.models import User


class UserCreateView(CreateView):
    form_class = UserCreateForm
    model = User
    template_name_suffix = '_create_form'


class UserDetailView(DetailView):
    model = User


class UserListView(ListView):
    model = User


class UserUpdateView(UpdateView):
    form_class = UserUpdateForm
    model = User
    template_name_suffix = '_update_form'
