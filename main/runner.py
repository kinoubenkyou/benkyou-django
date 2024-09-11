from django.conf import settings
from django.test.runner import DiscoverRunner
from mongoengine import connect, disconnect


class Runner(DiscoverRunner):
    def setup_test_environment(self, **kwargs):
        return_ = super().setup_test_environment(**kwargs)
        settings.CACHES["default"]["LOCATION"] = "redis://redis:6379/1"
        settings.CELERY_BROKER_URL = "redis://redis:6379/3"
        settings.CELERY_TASK_ALWAYS_EAGER = True
        settings.MONGO["db"] = f"test_{settings.MONGO["db"]}"
        return return_

    def setup_databases(self, **kwargs):
        return_ = super().setup_databases(**kwargs)
        disconnect()
        connect(**settings.MONGO)
        return return_
