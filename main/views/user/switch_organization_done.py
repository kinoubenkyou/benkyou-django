from django.views.generic import TemplateView


class UserSwitchOrganizationDoneView(TemplateView):
    template_name = "main/user/switch_organization_done.html"
