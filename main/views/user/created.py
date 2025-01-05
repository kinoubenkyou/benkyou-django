from django.views.generic.base import TemplateView


class UserCreatedView(TemplateView):
    template_name = "user/created.html"  # type: ignore[assignment]
