from django.conf import settings
from django.test.runner import DiscoverRunner


class Runner(DiscoverRunner):
    def setup_test_environment(self, **kwargs):
        result = super().setup_test_environment(**kwargs)
        settings.CACHES["default"]["LOCATION"] = "redis://redis:6379/1"
        return result
