from django.db.models import Model, ForeignKey, CASCADE, CharField


class Staff(Model):
    STATUSES = {
        "requested": "Requested",
        "invited": "Invited",
        "accepted": "Accepted",
    }

    organization = ForeignKey("Organization", on_delete=CASCADE)
    user = ForeignKey("User", on_delete=CASCADE)
    status = CharField(choices=STATUSES, max_length=256)
