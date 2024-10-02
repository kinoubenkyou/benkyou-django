from django.forms import ChoiceField, Form, IntegerField


class OrganizationActivityListForm(Form):
    SORT_CHOICES = (
        ("", ""),
        ("-timestamp", "timestamp desc"),
        ("timestamp", "timestamp asc"),
    )

    per_page = IntegerField(min_value=1, required=False)
    sort_by = ChoiceField(choices=SORT_CHOICES, required=False)
