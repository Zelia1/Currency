from currency.views import (bank_create, bank_delete,  bank_details, bank_update, banks,
                            contact_delete, contactus_create, contactus_details, contactus_list,
                            contactus_update, hello_world,)

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('first-app/', hello_world),
    path('currency/banks/', banks),
    path('currency/banks/details/<int:pk>/', bank_details),
    path('currency/contactus/', contactus_list),
    path('currency/contactus/details/<int:pk>/', contactus_details),
    path('currency/contactus/create/', contactus_create),
    path('currency/contactus/update/<int:pk>/', contactus_update),
    path('currency/contactus/delete/<int:pk>/', contact_delete),
    path('currency/bank/create/', bank_create),
    path('currency/bank/update/<int:pk>/', bank_update),
    path('currency/bank/delete/<int:pk>/', bank_delete)
]
