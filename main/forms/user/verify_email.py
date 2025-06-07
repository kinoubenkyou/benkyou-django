from typing import Any, Iterable, Mapping

from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
from django.forms import Form
from django.forms.fields import CharField
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
from django.utils.datastructures import MultiValueDict

from main.models import User


class UserVerifyEmailForm(Form):
    token = CharField()

    def __init__(
        self,
        user: User,
        data: Mapping[str, Any] | None = None,
        files: MultiValueDict[str, UploadedFile] | None = None,
        auto_id: bool | str = "id_%s",
        prefix: str | None = None,
        initial: Mapping[str, Any] | None = None,
        error_class: type[ErrorList] = ErrorList,
        label_suffix: str | None = None,
        empty_permitted: bool = False,
        field_order: Iterable[str] | None = None,
        use_required_attribute: bool | None = None,
        renderer: BaseRenderer | None = None,
    ):
        """Initialize form with user id."""
        self.user = user
        super().__init__(
            data,
            files,
            auto_id,
            prefix,
            initial,
            error_class,
            label_suffix,
            empty_permitted,
            field_order,
            use_required_attribute,
            renderer,
        )

    def clean_token(self) -> Any:
        """Validate with token in the cache."""
        token = self.cleaned_data["token"]
        sentinel = object()
        cached_token = cache.get(f"verify_user_email.{self.user.id}", sentinel)
        if cached_token is sentinel:
            raise ValidationError("token not found")
        elif cached_token != token:
            raise ValidationError("incorrect token")
        return token
