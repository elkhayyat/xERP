from abc import abstractmethod, ABC

from django.utils.translation import gettext as _

from authentication.repositories.user_repository import UserRepository
from profile.repositories.profile import ProfileRepository


class AbstractCreateAccountService(ABC):
    def __init__(self):
        self.user_repository = UserRepository()
        self.user = None

    @abstractmethod
    def creator_has_permission(self):
        pass

    def _register(self, password, email, phone, first_name, last_name, is_staff=False, is_superuser=False,
                  created_by=None):
        self.created_by = created_by
        if not self.creator_has_permission():
            raise PermissionError(_('You do not have permission to create account'))
        self.user = self.user_repository.create_user(
            password=password, email=email, phone=phone, first_name=first_name, last_name=last_name,
            is_staff=is_staff, is_superuser=is_superuser
        )
        self._create_profile()
        return self.user

    def _create_profile(self, birth_date=None, bio=None, image=None):
        return ProfileRepository(self.user).create_user_profile(birth_date=birth_date, bio=bio, image=image)


class UserRegisterService(AbstractCreateAccountService):
    def creator_has_permission(self):
        return True

    def register(self, password, email, phone, first_name, last_name):
        return self._register(password, email, phone, first_name, last_name)


class CreateStaffAccountService(AbstractCreateAccountService):

    def creator_has_permission(self):
        return self.created_by and self.created_by.is_active and self.created_by.is_staff

    def register(self, creator, password, email, phone, first_name, last_name):
        self._register(password, email, phone, first_name, last_name, is_staff=True, created_by=creator)


class CreateSuperAdminService(AbstractCreateAccountService):

    def creator_has_permission(self):
        return self.created_by and self.created_by.is_active and self.created_by.is_superuser

    def register(self, creator, password, email, phone, first_name, last_name):
        self._register(password, email, phone, first_name, last_name, is_staff=True, is_superuser=True,
                       created_by=creator)
