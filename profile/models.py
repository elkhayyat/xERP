from django.db import models
from django.utils.translation import gettext_lazy as _

from authentication.models import User
from core.db.fields import BirthdateField
from core.db.models import BaseModel, BaseTextChoices


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name=_('User'))
    image = models.ImageField(upload_to='users/', null=True, blank=True, verbose_name=_('Image'))
    birth_date = BirthdateField(required=True, minimum_age=13, verbose_name=_('Birth Date'))
    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name=_('Bio'))
    location = models.CharField(max_length=30, blank=True, null=True, verbose_name=_('Location'))

    def __str__(self):
        return self.user.phone.as_e164


class SocialLink(BaseModel):
    class SocialLinkChoices(BaseTextChoices):
        FACEBOOK = 'facebook', _('Facebook')
        X = 'x', _('X')
        INSTAGRAM = 'instagram', _('Instagram')
        LINKEDIN = 'linkedin', _('LinkedIn')
        GITHUB = 'github', _('GitHub')
        WEBSITE = 'website', _('Website')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_links', verbose_name=_('User'))
    link_type = SocialLinkChoices.model_field()
    url = models.URLField(verbose_name=_('URL'))

    def __str__(self):
        return self.link_type.description
