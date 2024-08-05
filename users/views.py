import random
import string

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, UpdateView

from users.forms import UserRegisterForm, EditingProfileForm
from users.models import User

import secrets


# Create your views here.
class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/user/email-confirm/{token}/'

        send_mail(subject='Подтверждение почты',
                  message=f'Здравствуйте, чтобы подтвердить свою почту перейдите по ссылке {url}',
                  from_email=mail,
                  recipient_list=[user.email],)
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class ResetTemplateView(TemplateView):
    template_name = 'user_forgot_password.html'

    def password_generation(self, length):
        return ''.join(
            random.choices(
                string.ascii_letters + string.digits,
                k=length
            )
        )

    def post(self, request):
        if request.method == 'POST':
            email = request.POST.get('email')
            user = User.objects.get(email=email)
            new_password = self.password_generation(10)
            user.set_password(new_password)
            user.save()
            host = self.request.get_host()
            send_mail(subject=f'Изменение пароля от почты {email}',
                      message=f'Здравствуйте, ваш новый пароль - {new_password}',
                      from_email=mail,
                      recipient_list=[email], )
        return render(request, 'contacts.html')


class ProfileView(UpdateView):
    model = User
    form_class = EditingProfileForm
    success_url = reverse_lazy('users:profile')
    template_name = 'users/editing_profile.html'

    def get_object(self, queryset=None):
        return self.request.user