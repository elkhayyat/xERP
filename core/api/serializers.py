from rest_framework import serializers

from core.db.validators import BirthdateValidator


class BaseUIDSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True, source='uid')

    class Meta:
        model = None
        fields = ['id']


class BirthdateSerializer(serializers.DateField):
    def __init__(self, value=None, minimum_age=0, allow_future_date=False, **kwargs):
        self.minimum_age = minimum_age
        self.allow_future_date = allow_future_date
        self.value = value
        super().__init__(**kwargs)

    def to_representation(self, value):
        return value.strftime('%Y-%m-%d')

    def to_internal_value(self, data):
        return data

    def validate(self, value):
        BirthdateValidator(value=value, minimum_age=self.minimum_age, required=self.required,
                           allow_future_date=self.allow_future_date).validate()
        return value
