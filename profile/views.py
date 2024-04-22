from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from django.views.generic import TemplateView, UpdateView
from rest_framework import generics

from profile.forms import EditProfileForm
from profile.serializers import ProfileSerializer


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile/profile.html'


class EditProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'profile/edit_profile.html'
    form_class = EditProfileForm

    def get_object(self, queryset=None):
        return self.request.user


class ProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = ProfileSerializer.Meta.model.objects.all()
    success_message = _('Profile updated successfully')

    def get_object(self):
        if self.request.user.is_authenticated:
            print(self.request.META.get('HTTP_AUTHORIZATION'))
            print(self.request.user)
            return self.request.user.profile
        else:
            raise PermissionError(_('User is not authenticated'))
