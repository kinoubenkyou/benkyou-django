from typing import Any

from django.conf import settings
from django.test.runner import DiscoverRunner as DjangoDiscoverRunner


class DiscoverRunner(DjangoDiscoverRunner):
    def setup_test_environment(self, **kwargs: Any) -> None:
        """Set cache to another Redis logical database."""
        return_ = super().setup_test_environment(**kwargs)
        settings.CACHES["default"]["LOCATION"] = (
            f"{settings.CACHES['default']['LOCATION']}/1"
        )
        settings.CELERY_TASK_ALWAYS_EAGER = True
        return return_
