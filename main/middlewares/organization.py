from main.models import Organization


class OrganizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            request.organization = Organization.objects.get(
                id=request.session.get("organization_id"),
            )
        except Organization.DoesNotExist:
            request.organization = None
        return self.get_response(request)
