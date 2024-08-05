from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.apps import UsersConfig

from django.conf import settings
from django.conf.urls.static import static

from users.views import UserCreateView, email_verification, ResetTemplateView, ProfileView
app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('forgot-password/', ResetTemplateView.as_view(), name='forgot-password'),
    path('profile/', ProfileView.as_view(), name='profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)