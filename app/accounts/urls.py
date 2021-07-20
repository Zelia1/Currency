from accounts import views

from django.contrib.auth import views as auth_views
from django.urls import path


app_name = 'account'

urlpatterns = [
    path('my-profile/<int:pk>/', views.MyProfile.as_view(), name='my-profile'),
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html'), name='reset-password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'), name='reset-password-sent'),
    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'),
         name='reset-password-confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'),
         name='reset-password-complete'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('activate/account/<uuid:activation_key>/', views.ActivateAccount.as_view(), name='activate-account'),
]
