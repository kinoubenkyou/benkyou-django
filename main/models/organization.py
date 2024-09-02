from django.db.models import Model, CharField, ManyToManyField


class Organization(Model):
    code = CharField(max_length=256, unique=True)
    name = CharField(max_length=256)
    users = ManyToManyField("User", through="Staff")
