from django.db.models import CharField, Model


class Organization(Model):
    code = CharField(unique=True)
    name = CharField()

    def __str__(self) -> str:
        """Get name."""
        return self.name
