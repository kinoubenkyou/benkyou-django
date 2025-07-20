from django.db.models import CASCADE, ForeignKey, Model


class OrganizationUser(Model):
    organization = ForeignKey("Organization", on_delete=CASCADE)
    user = ForeignKey("User", on_delete=CASCADE)
