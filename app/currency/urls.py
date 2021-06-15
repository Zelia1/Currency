from currency.views import (bank_create, bank_delete, bank_details, bank_update, banks,
                            contact_delete, contactus_create, contactus_details, contactus_list,
                            contactus_update,)

from django.urls import path

app_name = 'currency'

urlpatterns = [
    path('banks/', banks, name='banks'),
    path('banks/details/<int:pk>/', bank_details, name='bank-details'),
    path('contactus/', contactus_list, name='contactus-list'),
    path('contactus/details/<int:pk>/', contactus_details, name='contactus-details'),
    path('contactus/create/', contactus_create, name='contactus-create'),
    path('contactus/update/<int:pk>/', contactus_update, name='contactus-update'),
    path('contactus/delete/<int:pk>/', contact_delete, name='contact-delete'),
    path('bank/create/', bank_create, name='bank-create'),
    path('bank/update/<int:pk>/', bank_update, name='bank-update'),
    path('bank/delete/<int:pk>/', bank_delete, name='bank-delete')
]