from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView

from .forms import UserRegisterForm, UserLoginForm, UserUpdateForm


class RegisterUser(CreateView):
    form_class = UserRegisterForm
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.username = user.email
        user.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = 'login.html'


class UpdateUser(LoginRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    template_name = 'profile.html'

    def get_object(self, queryset=None):
        return get_user_model().objects.get(username=self.request.user.username)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.username = user.email
        user.save()
        return redirect('profile')
