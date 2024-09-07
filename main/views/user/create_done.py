from django.views.generic import TemplateView


class UserCreateDoneView(TemplateView):
    template_name = "main/user/create_done.html"
