import datetime

from django.contrib.auth import user_logged_in, login
from django.shortcuts import redirect, render
from django.utils import timezone
from django.utils.translation import gettext as _
from django.views.generic import View
from knox import views as knox_views
from knox.models import AuthToken
from knox.settings import knox_settings
from rest_framework import generics, permissions

from authentication.repositories.user_repository import UserRepository
from authentication.serializers import LoginSerializer, UserSerializer
from authentication.services.register import UserRegisterService
from core.api.api_responses import SuccessAPIResponse


class RegisterView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

    def post(self, request):
        user_repository = UserRepository()
        register_service = UserRegisterService()
        next_url = request.GET.get('next', None)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = register_service.register(password=password, email=email, phone=phone, first_name=first_name,
                                             last_name=last_name)
        if user_obj:
            return render(request, 'authentication/register.html', {'error': _('User already exists')})
        user_repository.create_user(first_name=first_name, last_name=last_name, phone=phone, email=email,
                                    password=password)
        return redirect(next_url or 'authentication:login')


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = serializer.data
            message = _('User created successfully')
            return SuccessAPIResponse(data=data, message=message)


class LoginAPIView(knox_views.LoginView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        remember_me = serializer.validated_data.get('remember_me', False)
        login(request, user)
        token_limit_per_user = self.get_token_limit_per_user()
        if token_limit_per_user is not None:
            now = timezone.now()
            token = user.auth_token_set.filter(expiry__gt=now)
            if token.count() >= token_limit_per_user:
                raise Exception(_('Maximum amount of tokens allowed per user exceeded.'))
        token_ttl = self.get_token_ttl(remember_me)
        instance, token = AuthToken.objects.create(user, token_ttl)
        user_logged_in.send(sender=user.__class__,
                            request=request, user=user)
        data = self.get_post_response_data(request, token, instance)
        return SuccessAPIResponse(message=_('Logged in successfully'), data=data)

    def get_token_ttl(self, long_lived=False):
        if long_lived:
            return datetime.timedelta(days=30)
        return datetime.timedelta(hours=10)

    def get_post_response_data(self, request, token, instance):
        user_serializer = self.get_user_serializer_class()

        data = {
            'expiry': self.format_expiry_datetime(instance.expiry),
            'token': token
        }
        if user_serializer is not None:
            data["user"] = user_serializer(
                request.user,
                context=self.get_context()
            ).data
        return data


class LogoutAllView(knox_views.LogoutAllView):

    def post(self, request, format=None):
        super().post(request, format)
        return SuccessAPIResponse(message=_('Logged out successfully'))


class LogoutView(knox_views.LogoutView):
    def post(self, request, format=None):
        super().post(request, format)
        return SuccessAPIResponse(message=_('Logged out successfully'))
