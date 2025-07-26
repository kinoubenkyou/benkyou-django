from typing import Any
from urllib.parse import urlsplit, urlunsplit

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.http import HttpRequest, HttpResponseBase, HttpResponseRedirect, QueryDict
from django.shortcuts import resolve_url
from django.views import View


class OrganizationSwitchedMixin(View):
    organization_id: str | int

    def dispatch(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> HttpResponseBase:
        """Redirect to switch organization if not yet switched, else set organization id."""  # noqa: E501
        organization_id = self.request.session.get("organization_id")
        if organization_id is None:
            url_parts = list(urlsplit(resolve_url("organization-switch")))
            querystring = QueryDict(url_parts[3], mutable=True)
            querystring[REDIRECT_FIELD_NAME] = self.request.get_full_path()
            url_parts[3] = querystring.urlencode(safe="/")
            return HttpResponseRedirect(urlunsplit(url_parts))
        self.organization_id = organization_id
        return super().dispatch(request, *args, **kwargs)
