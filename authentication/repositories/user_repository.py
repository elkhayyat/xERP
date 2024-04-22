from authentication.models import User
from authentication.querysets import UserQuerySet


class UserRepository:
    def __init__(self, user=None):
        self.user = user

    @staticmethod
    def create_user(first_name, last_name, email, phone, password, is_staff=False, is_superuser=False):
        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, phone=phone,
                                        password=password, is_staff=is_staff, is_superuser=is_superuser)

        return user

    def filter_users(self, queryset, **kwargs):
        users = queryset
        for key, value in kwargs.items():
            if hasattr(self.user, key) and value is not None:
                self.user = self.user.filter(**{key: value})
        return users

    def get_user_by_uid(self, uid, queryset=UserQuerySet.all()):
        return self.filter_users(queryset=queryset, uid=uid).first()

    def get_user_by_email(self, email):
        return self.filter_users(User.objects.all(), email=email).first()

    def get_user_by_phone(self, phone):
        return self.filter_users(User.objects.all(), phone=phone).first()

    def get_user_by_email_or_phone(self, username_or_email_or_phone):
        return self.filter_users(User.objects, username=username_or_email_or_phone).first() or \
            self.filter_users(User.objects, email=username_or_email_or_phone).first() or \
            self.filter_users(User.objects, phone=username_or_email_or_phone).first()
