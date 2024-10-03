from django.forms import ChoiceField, DateTimeField, Form, IntegerField

from main.forms.fields import PlusOneDayDateTimeField, UserEmailField
from main.forms.inputs import DateInput


class ActivitiesListForm(Form):
    SORT_CHOICES = (
        ("", ""),
        ("-timestamp", "timestamp desc"),
        ("timestamp", "timestamp asc"),
    )

    per_page = IntegerField(min_value=1, required=False)
    sort_by = ChoiceField(choices=SORT_CHOICES, required=False)
    timestamp__gte = DateTimeField(label="From date", required=False, widget=DateInput)
    timestamp__lt = PlusOneDayDateTimeField(
        label="To date",
        required=False,
        widget=DateInput,
    )
    user_id = UserEmailField(label="User email", required=False)
