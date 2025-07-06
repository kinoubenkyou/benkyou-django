from django.db.models import CharField, Model


class Organization(Model):
    code = CharField(unique=True)
    name = CharField()
