from currency.views import (bank_details,
                            banks,
                            contactus_list,
                            hello_world)

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('first-app/', hello_world),

    path('currency/banks/', banks),

    path('currency/banks/details/<int:pk>/', bank_details),

    path('currency/contactus/', contactus_list)
]
