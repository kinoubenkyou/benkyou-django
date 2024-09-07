from django.forms import ModelForm

from main.models import Organization


class OrganizationUpdateForm(ModelForm):
    class Meta:
        model = Organization
        fields = ("code", "name")
