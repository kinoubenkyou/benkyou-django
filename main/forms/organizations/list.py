from django.forms import CharField, ChoiceField

from main.forms.list import ListForm, get_sort_choices


class OrganizationsListForm(ListForm):
    class Meta:
        filter_fields = ("code__icontains", "name__icontains")
        sort_choices = get_sort_choices(("code", "name"))

    code__icontains = CharField(required=False)
    name__icontains = CharField(required=False)
    sort_by = ChoiceField(choices=Meta.sort_choices, required=False)
