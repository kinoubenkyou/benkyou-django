from django.forms import ChoiceField

from main.documents import OrganizationActivity
from main.forms import ActivitiesListForm


class OrganizationActivitiesListForm(ActivitiesListForm):
    ACTION_CHOICES = (("", ""), *OrganizationActivity.ACTION_CHOICES)

    action = ChoiceField(choices=ACTION_CHOICES, required=False)
