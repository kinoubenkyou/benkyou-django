from typing import TYPE_CHECKING, Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import RedirectURLMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView

from main.forms.organization.switch import OrganizationSwitchForm

if TYPE_CHECKING:
    FormView_ = FormView[OrganizationSwitchForm]  # pragma: no cover
else:
    FormView_ = FormView


class OrganizationSwitchView(LoginRequiredMixin, RedirectURLMixin, FormView_):
    form_class = OrganizationSwitchForm
    next_page = reverse_lazy("user-read")
    template_name = "form.html"

    def form_valid(self, form: OrganizationSwitchForm) -> HttpResponse:
        """Set organization id in session."""
        self.request.session["organization_id"] = form.cleaned_data["organization"].id
        return super().form_valid(form)

    def get_form_kwargs(self) -> dict[str, Any]:
        """Pass user to form."""
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs
