from django.forms import Form, CharField, HiddenInput


class UserVerifyEmailForm(Form):
    token = CharField(widget=HiddenInput)
