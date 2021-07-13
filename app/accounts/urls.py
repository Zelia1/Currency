from accounts import views

from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('my-profile/<int:pk>/', views.MyProfile.as_view(), name='my-profile'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset-password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='reset-password-done'),
    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='reset-password-confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),
         name='reset-password-complete'),
]
