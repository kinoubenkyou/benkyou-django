from django.views.generic import TemplateView


class UserSignInDoneView(TemplateView):
    template_name = "main/user/sign_in_done.html"
