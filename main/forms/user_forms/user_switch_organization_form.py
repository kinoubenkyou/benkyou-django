from django.forms import Form, ModelChoiceField


class UserSwitchOrganizationForm(Form):
    organization = ModelChoiceField(empty_label=None, queryset=None, required=True)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["organization"].queryset = user.organizations.all()
