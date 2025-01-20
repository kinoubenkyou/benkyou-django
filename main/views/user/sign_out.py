from django.contrib.auth.views import LogoutView


class UserSignOutView(LogoutView):
    http_method_names = ["get", *LogoutView.http_method_names]
    template_name = "form.html"
