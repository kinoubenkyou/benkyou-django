from main.models import Organization


class OrganizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.organization = Organization.objects.filter(
            id=request.session.get("organization_id")
        ).first()
        return self.get_response(request)
