from django.db import models

from core.db.validators import BirthdateValidator


class MoneyField(models.DecimalField):
    def __init__(self, *args, **kwargs):
        kwargs['max_digits'] = 20
        kwargs['decimal_places'] = 2
        kwargs['default'] = 0.00
        super().__init__(*args, **kwargs)


class BirthdateField(models.DateField):
    def __init__(self, minimum_age=0, allow_future_date=False, required=False, *args, **kwargs):
        self.minimum_age = minimum_age
        self.allow_future_date = allow_future_date
        self.required = required
        super().__init__(*args, **kwargs)

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        BirthdateValidator(value=value, minimum_age=self.minimum_age, required=self.required).validate()
