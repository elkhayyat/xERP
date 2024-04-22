from django.core.exceptions import ValidationError
from django.utils import timezone

from core import strings


class BirthdateValidator:
    def __init__(self, value=None, minimum_age=0, required=False, allow_future_date=False):
        self.value = value
        self.minimum_age = minimum_age
        self.required = required
        self.allow_future_date = allow_future_date

    def validate(self):
        validators = [
            self.validate_required,
            self.validate_in_future,
            self.validate_minimum_age
        ]
        for validator in validators:
            validator()

    def validate_in_future(self):
        if not self.allow_future_date and self.value > timezone.now().date():
            raise ValidationError(strings.BIRTHDATE_CAN_NOT_BE_IN_THE_FEATURE)

    def validate_minimum_age(self):
        if self.value is not None and (timezone.now().date() - self.value).days < self.minimum_age * 365:
            raise ValidationError(strings.AGE_MUST_BE_AT_LEAST_X_YEARS_OLD(self.minimum_age))

    def validate_required(self):
        if self.value is None and self.required:
            raise ValidationError(strings.THIS_FIELD_IS_REQUIRED)
