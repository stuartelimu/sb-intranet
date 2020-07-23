from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponse

from .forms import RegistrationForm, UserForm, ProfileForm
from .models import User, Profile


class RegistrationView(View):
    template_name = 'register.html'
    form_class = RegistrationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.team = form.cleaned_data.get('team')
            user.save()
            return redirect('login')
        else:
            return render(request, self.template_name, {'form': form})


class ProfileView(LoginRequiredMixin, View):
    template_name = 'profile.html'
    user_form = UserForm
    profile_form = ProfileForm

    def get(self, request, *args, **kwargs):
        user_form = self.user_form(instance=request.user)
        profile_form = self.profile_form(instance=request.user.profile)
        return render(request, self.template_name, {'user_form': user_form, 'profile_form':profile_form})

    def post(self, request, *args, **kwargs):
        user_form = self.user_form(request.POST, instance=request.user)
        profile_form = self.profile_form(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')

        return render(request, self.template_name, {'user_form': user_form, 'profile_form':profile_form})

