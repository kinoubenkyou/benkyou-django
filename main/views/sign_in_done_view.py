from django.views.generic import TemplateView


class SignInDoneView(TemplateView):
    template_name = "main/sign_in_done.html"
