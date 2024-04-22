from django.db import models


class UserQuerySet(models.QuerySet):
    @classmethod
    def all(cls):
        return cls

    @classmethod
    def active(self):
        return self.filter(is_active=True)

    def inactive(self):
        return self.filter(is_active=False)

    def deleted(self):
        return self.filter(is_deleted=True)

    def not_deleted(self):
        return self.filter(is_deleted=False)

    def tenant_users(self, tenant):
        return self.filter(tenant=tenant)

    def customers(self):
        return self.filter(is_staff=False, is_superuser=False)

    def staff(self):
        return self.filter(is_staff=True)

    def superusers(self):
        return self.filter(is_superuser=True)
