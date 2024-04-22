import uuid

from django.core.exceptions import ValidationError
from django.db import models


class UUIDModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModel(UUIDModel, TimeStampModel, SoftDeleteModel):
    class Meta:
        abstract = True


class BaseTextChoices(models.TextChoices):

    @classmethod
    def max_length(cls) -> int:
        return max(len(value) for value in cls.values)

    @classmethod
    def model_field(cls, verbose_name: str = None, default: 'models.TextChoices' = None) -> models.CharField:
        return models.CharField(verbose_name=verbose_name, max_length=cls.max_length(),
                                choices=cls.choices, default=default)

    @classmethod
    def serialize_choices(cls):
        return [{'value': value, 'label': label} for value, label in cls.choices]

