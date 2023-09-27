import random

from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from config import settings
from users.forms import UserForm, UserRegisterForm, UserLoginForm
from users.models import User
from users.settings import create_password


class LoginView(BaseLoginView):
	form_class = UserLoginForm
	template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
	pass


class RegisterView(CreateView):
	model = User
	form_class = UserRegisterForm
	success_url = reverse_lazy('users:login')
	template_name = 'users/register.html'

	def form_valid(self, form):
		new_user = form.save()
		send_mail(
			subject='Congratulations with registration',
			message='You registered on our website!',
			from_email=settings.EMAIL_HOST_USER,
			recipient_list=[new_user.email]
		)
		return super().form_valid(form)


class UserUpdateView(UpdateView):
	model = User
	form_class = UserForm
	success_url = reverse_lazy('users:profile')

	def get_object(self, queryset=None):
		return self.request.user


def generate_password(request):
	new_password = create_password()
	request.user.set_password(new_password)
	request.user.save()
	message = f'You registered new password on our website: {new_password}'

	send_mail(
		subject='New Password',
		message=f'You registered new password on our website: {new_password}',
		from_email=settings.EMAIL_HOST_USER,
		recipient_list=[request.user.email]
	)

	return redirect(reverse('catalog:index'))
