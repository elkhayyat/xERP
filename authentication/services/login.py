from abc import ABC, abstractmethod

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password

from authentication.repositories.user_repository import UserRepository


class AbstractLoginService(ABC):
    def __init__(self):
        self.repository = UserRepository()

    @staticmethod
    @abstractmethod
    def can_login(user) -> bool:
        pass

    def login(self, username: str, password: str) -> bool:
        user = self.repository.get_user_by_email_or_phone(username)
        user = authenticate(username=user.username, password=password)
        if not self.can_login(user):
            return False
        if check_password(password, user.password):
            return user
        return False


class UserLoginService(AbstractLoginService):
    @staticmethod
    def can_login(user) -> bool:
        return user and user.is_active


class StaffLoginService(AbstractLoginService):
    @staticmethod
    def can_login(user) -> bool:
        return user and user.is_active and (user.is_staff or user.is_superadmin)
