from datetime import datetime

from mongoengine import DateTimeField, LongField


class Activity:
    meta = {"index": ["object_id"]}

    object_id = LongField(min_value=1, required=True)
    timestamp = DateTimeField(default=datetime.now, required=True)
    user_id = LongField(min_value=1, required=True)
