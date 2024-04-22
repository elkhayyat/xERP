from django.utils.translation import gettext_lazy as _

BIRTHDATE_CAN_NOT_BE_IN_THE_FEATURE = _("Birthdate can not be in the feature")
THIS_FIELD_IS_REQUIRED = _("This field is required.")


def AGE_MUST_BE_AT_LEAST_X_YEARS_OLD(minimum_age=0):
    return _(f"Age must be at least {minimum_age} years old.")
