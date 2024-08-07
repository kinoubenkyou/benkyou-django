from django import template
from django.urls import reverse
from django.utils.http import urlencode

register = template.Library()


@register.simple_tag(takes_context=True)
def elided_page_range(context):
    return context["page_obj"].paginator.get_elided_page_range(
        number=context["page_obj"].number, on_each_side=0, on_ends=1
    )


@register.simple_tag(takes_context=True)
def url_by_ordering(context, ordering, view_name):
    query_dict = {
        query_key: context[query_key]
        for query_key in ("email__icontains", "name__icontains")
        if query_key in context
    }
    query_dict["ordering"] = (
        f"-{ordering}" if ordering == context.get("ordering") else f"{ordering}"
    )
    return f"{reverse(view_name)}?{urlencode(query_dict)}"


@register.simple_tag(takes_context=True)
def url_by_page(context, page_number, view_name):
    query_dict = {
        query_key: context[query_key]
        for query_key in (
            "email__icontains",
            "name__icontains",
            "ordering",
        )
        if query_key in context
    }
    query_dict["page"] = page_number
    return f"{reverse(view_name)}?{urlencode(query_dict)}"
