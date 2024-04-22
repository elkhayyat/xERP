from profile.models import Profile


class ProfileRepository:
    def __init__(self, user):
        self.user = user

    def create_user_profile(self, birth_date=None, bio=None, image=None):
        profile = Profile.objects.create(user=self.user, birth_date=birth_date, bio=bio, image=image)
        return profile

    def get_profile(self):
        return self.user.profile

    def update_profile(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self.user.profile, key, value)
        self.user.profile.save()
        return self.user.profile
