from django.views.generic import TemplateView


class UserCreateDoneView(TemplateView):
    template_name = "main/user_create_done.html"
