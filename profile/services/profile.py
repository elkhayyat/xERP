from profile.repositories.profile import ProfileRepository


class ProfileService:
    def __init__(self, user):
        self.user = user
        self.profile_repository = ProfileRepository(user)
        self.profile = self.profile_repository.get_profile()

    def get_user_profile(self):
        self.profile = self.profile_repository.get_profile()
        return self.profile

    def update_user_profile(self, birth_date=None, bio=None, avatar=None):
        self.profile = self.profile_repository.update_profile(birth_date=birth_date, bio=bio, avatar=avatar)
        return self.profile

    def get_empty_social_links(self):
        return self.profile_repository.get_empty_social_links()