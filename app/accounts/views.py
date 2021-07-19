from accounts.models import User

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
# from django.shortcuts import render

# Create your views here.


# from django.contrib.auth.forms import PasswordResetForm


class MyProfile(LoginRequiredMixin, UpdateView):
    queryset = User.objects.all()
    template_name = 'my-profile.html'
    success_url = reverse_lazy('index')
    fields = (
        'first_name',
        'last_name',
    )

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.request.user.pk)
        return queryset


# class ResetPassword(PasswordResetForm):
#     queryset = User.objects.all()
#     template_name = 'registration/password_reset_form.html'
