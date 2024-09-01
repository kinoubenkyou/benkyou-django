from django.conf import settings
from django.test.runner import DiscoverRunner


class Runner(DiscoverRunner):
    def setup_test_environment(self, **kwargs):
        return_ = super().setup_test_environment(**kwargs)
        settings.CACHES["default"]["LOCATION"] = "redis://redis:6379/1"
        settings.CELERY_BROKER_URL = "redis://redis:6379/3"
        settings.CELERY_TASK_ALWAYS_EAGER = True
        return return_
