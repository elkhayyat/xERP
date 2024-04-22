from django.urls import path

from profile import views as profile_views

app_name = "profile"

urlpatterns = [

    path('', profile_views.ProfileView.as_view(), name='profile'),
    path('edit/', profile_views.EditProfileView.as_view(), name='edit_profile'),
    path('api/', profile_views.ProfileAPIView.as_view(), name='api_profile'),
]
