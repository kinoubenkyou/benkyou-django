from django.forms import Form, ModelMultipleChoiceField


class UserSwitchOrganizationForm(Form):
    organization = ModelMultipleChoiceField(queryset=None, required=True)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["organization"].queryset = user.organizations.all()
