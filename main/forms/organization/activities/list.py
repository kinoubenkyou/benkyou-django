from django.forms import ChoiceField, Form


class OrganizationActivityListForm(Form):
    SORT_CHOICES = (
        ("", ""),
        ("-timestamp", "timestamp desc"),
        ("timestamp", "timestamp asc"),
    )

    sort_by = ChoiceField(choices=SORT_CHOICES, required=False)
