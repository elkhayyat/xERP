from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _
from knox.models import AuthToken
from phonenumber_field.modelfields import PhoneNumberField

from core.db.models import BaseModel


class CustomUserManager(UserManager):
    def _create_user(self, phone, email, password, **extra_fields):
        if not phone:
            raise ValueError(_('The given phone must be set'))
        if not email:
            raise ValueError(_('The given email must be set'))
        email = self.normalize_email(email)
        user = self.model(phone=phone, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, email=None, first_name=None, last_name=None, password=None, **extra_fields):
        # append first name and last name to extra fields
        extra_fields['first_name'] = first_name
        extra_fields['last_name'] = last_name
        return self._create_user(phone, email, password, **extra_fields)


class User(AbstractUser, BaseModel):
    username = None

    phone = PhoneNumberField(unique=True, verbose_name=_('Phone Number'))
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.phone.as_e164

    def get_token(self):
        _, token = AuthToken.objects.create(user=self)
        return token
