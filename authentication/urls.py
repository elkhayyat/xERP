from django.urls import path
from knox import views as knox_views

from authentication import views as customer_auth_views

app_name = 'authentication'

urlpatterns = [
    path('login/', customer_auth_views.LoginAPIView.as_view(), name='login'),
    path('register/', customer_auth_views.RegisterView.as_view(), name='register'),
    path('logout/all/', customer_auth_views.LogoutAllView.as_view(), name='logout_all'),
    path('logout/', customer_auth_views.LogoutView.as_view(), name='logout'),
]
