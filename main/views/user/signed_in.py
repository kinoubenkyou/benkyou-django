from django.views.generic.base import TemplateView


class UserSignedInView(TemplateView):
    template_name = "user/signed_in.html"  # type: ignore[assignment]
