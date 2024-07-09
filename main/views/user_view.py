from django.views.generic import CreateView, DetailView, ListView

from main.forms import UserCreateForm
from main.models import User


class UserCreateView(CreateView):
    form_class = UserCreateForm
    model = User
    template_name_suffix = '_create_form'


class UserDetailView(DetailView):
    model = User


class UserListView(ListView):
    model = User
