from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import RedirectURLMixin
from django.views.generic import FormView

from main.forms.organization import OrganizationSwitchForm


class OrganizationSwitchView(RedirectURLMixin, LoginRequiredMixin, FormView):
    form_class = OrganizationSwitchForm
    next_page = "/organization/"
    template_name = "main/organization/switch.html"

    def get_form_kwargs(self):
        return super().get_form_kwargs() | {"user": self.request.user}

    def form_valid(self, form):
        return_ = super().form_valid(form)
        self.request.session["organization_id"] = form.cleaned_data["organization"].id
        return return_
