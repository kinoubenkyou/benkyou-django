from datetime import datetime

from mongoengine import DateTimeField, LongField, QuerySet

from main.models import User


class ActivityQuerySet(QuerySet):
    def __init__(self, document, collection):
        self.selected_models = []
        super().__init__(document, collection)

    def _populate_cache(self):
        return_ = super()._populate_cache()
        if "user" in self.selected_models:
            users = {
                user.id: user
                for user in User.objects.filter(
                    id__in=[object_.user_id for object_ in self._result_cache],
                )
            }
            for object_ in self._result_cache:
                object_.user = users.get(object_.user_id)
        return return_

    def _clone_into(self, new_qs):
        return super()._clone_into(new_qs).select_models(*self.selected_models)

    def select_models(self, *models):
        self.selected_models.extend(models)
        return self


class Activity:
    meta = {"index": ["object_id"], "queryset_class": ActivityQuerySet}

    object_id = LongField(min_value=1, required=True)
    timestamp = DateTimeField(default=datetime.now, required=True)
    user_id = LongField(min_value=1, required=True)
