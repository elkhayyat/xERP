from django.db import models
from django.utils.translation import gettext_lazy as _

from authentication.models import User
from core.db.models import BaseModel, BaseTextChoices


class Log(BaseModel):
    class ActionChoices(BaseTextChoices):
        CREATE = 'create', _('Create')
        UPDATE = 'update', _('Update')
        DELETE = 'delete', _('Delete')
        LIST = 'list', _('List')
        VIEW = 'view', _('View')
        LOGIN = 'login', _('Login')
        LOGOUT = 'logout', _('Logout')
        FORGOT_PASSWORD = 'forgot_password', _('Forgot Password')
        REGISTER = 'register', _('Register')

    class ModuleChoices(BaseTextChoices):
        AUTHENTICATION = 'authentication', _('Authentication')
        PROFILE = 'profile', _('Profile')

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    action = ModuleChoices.model_field()
    module = ModuleChoices.model_field()
    object_uid = models.UUIDField(null=True, blank=True)
    object_name = models.CharField(max_length=100, null=True, blank=True)
    before = models.JSONField(null=True, blank=True)
    after = models.JSONField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
