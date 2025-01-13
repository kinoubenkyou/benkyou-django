from django.contrib.auth.views import LoginView


class UserSignInView(LoginView):
    template_name = "form.html"
