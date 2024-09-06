from django.views.generic import TemplateView


class UserSignOutDoneView(TemplateView):
    template_name = "main/user/sign_out_done.html"
