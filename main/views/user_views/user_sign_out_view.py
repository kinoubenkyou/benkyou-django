from django.contrib.auth.views import LogoutView


class UserSignOutView(LogoutView):
    http_method_names = LogoutView.http_method_names + ["get"]
    template_name = "main/user/sign_out.html"
