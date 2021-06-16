from currency.views import (BankCreateView, BankDetailView, BankUpdateView, BanksListView, DeleteView,
                            RateListView, contact_delete, contactus_create, contactus_details, contactus_list,
                            contactus_update)

from django.urls import path

app_name = 'currency'

urlpatterns = [
    path('rate/', RateListView.as_view(), name='rate-list'),
    path('banks/', BanksListView.as_view(), name='banks'),
    path('banks/details/<int:pk>/', BankDetailView.as_view(), name='bank-details'),
    path('contactus/', contactus_list, name='contactus-list'),
    path('contactus/details/<int:pk>/', contactus_details, name='contactus-details'),
    path('contactus/create/', contactus_create, name='contactus-create'),
    path('contactus/update/<int:pk>/', contactus_update, name='contactus-update'),
    path('contactus/delete/<int:pk>/', contact_delete, name='contact-delete'),
    path('bank/create/', BankCreateView.as_view(), name='bank-create'),
    path('bank/update/<int:pk>/', BankUpdateView.as_view(), name='bank-update'),
    path('bank/delete/<int:pk>/', DeleteView.as_view(), name='bank-delete')
]
