from django.forms import CharField, Form, HiddenInput


class UserVerifyEmailForm(Form):
    token = CharField(widget=HiddenInput)
