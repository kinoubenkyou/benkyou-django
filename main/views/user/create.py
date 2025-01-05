from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView

from main.forms.user import UserCreateForm


class UserCreateView(CreateView):
    form_class = UserCreateForm  # type: ignore[assignment]
    success_url = reverse_lazy("user-created")
    template_name = "form.html"  # type: ignore[assignment]
