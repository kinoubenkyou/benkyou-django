from django.forms import (
    ChoiceField,
    DateTimeField,
    Form,
    IntegerField,
    ModelChoiceField,
)

from main.forms.fields import PlusOneDayDateTimeField
from main.forms.inputs import DateInput
from main.models import User


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
    user = ModelChoiceField(queryset=User.objects.all(), required=False)

    def clean(self):
        return_ = super().clean()
        if return_["user"]:
            return_["user_id"] = return_.pop("user").id
        return return_
