from django.forms import ModelChoiceField

from main.forms.user import UserForm
from main.models import Organization


class OrganizationSwitchForm(UserForm):
    organization = ModelChoiceField(
        queryset=Organization.objects.none(), empty_label=None
    )

    def post_init(self) -> None:
        """Set organization choices."""
        self.fields["organization"].queryset = Organization.objects.filter(  # type: ignore[attr-defined]
            organizationuser__user=self.user
        )
