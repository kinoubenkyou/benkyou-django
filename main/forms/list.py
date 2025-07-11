from typing import Iterable

from django.forms import ChoiceField, Form, IntegerField


def get_sort_choices(choice_names: tuple[str, ...]) -> Iterable[tuple[str | None, str]]:
    """Get empty choice, ascending and descending choices for each choice name."""
    choices: list[tuple[str, str]] = [("id", "")]
    for choice_name in choice_names:
        choices.append((choice_name, f"{choice_name} ascending"))
        choices.append((f"-{choice_name}", f"{choice_name} descending"))
    return choices


class ListForm(Form):
    class Meta:
        filter_fields: tuple[str, ...] = tuple()
        sort_choices: Iterable[tuple[str | None, str]] = tuple()

    page_size = IntegerField(max_value=100, min_value=1)
    sort_by: ChoiceField
