from urllib.parse import urlparse, urlunparse

from django.http import HttpResponseRedirect, QueryDict


class OrganizationRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.organization:
            url_parts = list(urlparse("/user/switch_organization/"))
            querystring = QueryDict(url_parts[4], mutable=True)
            querystring["next"] = self.request.get_full_path()
            url_parts[4] = querystring.urlencode(safe="/")
            return HttpResponseRedirect(urlunparse(url_parts))
        return super().dispatch(request, *args, **kwargs)
