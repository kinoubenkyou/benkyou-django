from django.contrib.auth.views import PasswordChangeView


class UserChangePasswordView(PasswordChangeView):
    success_url = "/user/"
    template_name = "main/user/change_password.html"
