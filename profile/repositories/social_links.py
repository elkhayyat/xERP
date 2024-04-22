from profile.models import SocialLink


class SocialLinkRepository:
    def __init__(self, user):
        self.user = user

    def get_social_links(self):
        return self.user.social_links

    def create_social_link(self, link_type: SocialLink.SocialLinkChoices, url: str):
        social_link = SocialLink.objects.create(user=self.user, link_type=link_type, url=url)
        return social_link

    def not_used_social_links(self):

        for link in self.get_social_links():
            SocialLink.SocialLinkChoices.values.remove(link.link_type.values)