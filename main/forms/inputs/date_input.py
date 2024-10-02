from django.forms import DateInput as DjangoDateInput


class DateInput(DjangoDateInput):
    input_type = "date"
