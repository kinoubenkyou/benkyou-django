from mongoengine import (
    Document,
    DynamicEmbeddedDocument,
    EmbeddedDocumentField,
    StringField,
)

from main.documents.activity import Activity


class OrganizationActivityData(DynamicEmbeddedDocument):
    code = StringField(max_length=256)
    name = StringField(max_length=256)


class OrganizationActivity(Activity, Document):
    UPDATE_ACTION = "update"
    ACTION_CHOICES = ((UPDATE_ACTION, "Update"),)

    action = StringField(choices=ACTION_CHOICES, required=True)
    data = EmbeddedDocumentField(OrganizationActivityData)
