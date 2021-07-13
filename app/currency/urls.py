from currency.views import (BankCreateView, BankDeleteView, BankDetailView, BankUpdateView, BanksListView,
                            ContactDeleteView, ContactUsCreateView, ContactUsListView,
                            ContactUsUpdateView, ContactusDetailView, RateDetailView, RateDeleteView,
                            RateListView, RateUpdateView)

from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'currency'

urlpatterns = [
    path('rate/', RateListView.as_view(), name='rate-list'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/details/<int:pk>/', RateDetailView.as_view(), name='rate-details'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),
    path('banks/', BanksListView.as_view(), name='banks'),
    path('banks/details/<int:pk>/', BankDetailView.as_view(), name='bank-details'),
    path('contactus/', ContactUsListView.as_view(), name='contactus-list'),
    path('contactus/details/<int:pk>/', ContactusDetailView.as_view(), name='contactus-details'),
    path('contactus/create/', ContactUsCreateView.as_view(), name='contactus-create'),
    path('contactus/update/<int:pk>/', ContactUsUpdateView.as_view(), name='contactus-update'),
    path('contactus/delete/<int:pk>/', ContactDeleteView.as_view(), name='contact-delete'),
    path('bank/create/', BankCreateView.as_view(), name='bank-create'),
    path('bank/update/<int:pk>/', BankUpdateView.as_view(), name='bank-update'),
    path('bank/delete/<int:pk>/', BankDeleteView.as_view(), name='bank-delete'),
]
