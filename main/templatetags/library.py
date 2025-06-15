from typing import Any

from django.template import Library

register = Library()


@register.filter
def get_attribute(object_: object, attribute: str) -> Any:
    """Get object attribute."""
    return getattr(object_, attribute)
