from datetime import timedelta

from django.forms import DateTimeField


class PlusOneDayDateTimeField(DateTimeField):
    def to_python(self, value):
        return_ = super().to_python(value)
        return return_ + timedelta(days=1) if return_ else return_
