# from annoying.functions import get_object_or_None

from accounts.forms import SignUpForm
from accounts.models import User
from accounts.tokens import account_activation_token

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, RedirectView, UpdateView

# from django.contrib.auth.forms import PasswordResetForm


class MyProfile(LoginRequiredMixin, UpdateView):
    queryset = User.objects.all()
    template_name = 'my-profile.html'
    success_url = reverse_lazy('index')
    fields = (
        'first_name',
        'last_name',
        'avatar',
        'email',
    )

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.request.user.pk)
        return queryset


class SignUp(CreateView):
    model = User
    template_name = 'signup.html'
    success_url = reverse_lazy('index')
    form_class = SignUpForm


class ActivateAccount(RedirectView):
    pattern_name = 'index'

    def get_redirect_url(self, *args, **kwargs):
        activation_key = kwargs.pop('activation_key')
        activation_token = kwargs.pop('token')
        user = User.objects.get(username=activation_key)

        if user and account_activation_token.check_token(user, activation_token):
            if user.is_active:
                messages.warning(self.request, 'Your account is already active.')
            else:
                messages.info(self.request, 'Thanks for activating your account.')
                user.is_active = True
                user.save(update_fields=('is_active',))

        response = super().get_redirect_url(*args, **kwargs)
        return response

# class ResetPassword(PasswordResetForm):
#     queryset = User.objects.all()
#     template_name = 'registration/password_reset_form.html'
