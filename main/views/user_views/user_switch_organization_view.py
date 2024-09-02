from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView

from main.forms.user_forms import UserSwitchOrganizationForm


class UserSwitchOrganizationView(LoginRequiredMixin, FormView):
    form_class = UserSwitchOrganizationForm
    success_url = "/user/switch_organization/done/"
    template_name = "main/user/switch_organization.html"

    def get_form_kwargs(self):
        return super().get_form_kwargs() | {"user": self.request.user}

    def form_valid(self, form):
        return_ = super().form_valid(form)
        self.request.session["organization_id"] = form.cleaned_data["organization"][
            0
        ].id
        return return_
