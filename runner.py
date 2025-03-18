from typing import Any

from django.conf import settings
from django.test.runner import DiscoverRunner as DjangoDiscoverRunner


class DiscoverRunner(DjangoDiscoverRunner):
    def setup_test_environment(self, **kwargs: Any) -> None:
        """Set database."""
        return_ = super().setup_test_environment(**kwargs)
        settings.DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": settings.BASE_DIR / "db.sqlite3",
            }
        }
        return return_
