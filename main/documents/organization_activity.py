from mongoengine import (
    Document,
    DynamicEmbeddedDocument,
    EmbeddedDocumentField,
    StringField,
)

from main.documents.activity import Activity
from main.models import User


class OrganizationActivityData(DynamicEmbeddedDocument):
    code = StringField(max_length=256)
    name = StringField(max_length=256)


class OrganizationActivity(Activity, Document):
    UPDATE_ACTION = "update"
    ACTIONS = (UPDATE_ACTION,)

    action = StringField(choices=ACTIONS, required=True)
    data = EmbeddedDocumentField(OrganizationActivityData)

    def user(self):
        return User.objects.get(pk=self.user_id)
