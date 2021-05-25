from django.contrib import admin
from django.urls import path

from currency.views import my_first_app_django

urlpatterns = [
    path('admin/', admin.site.urls),

    path('first-app/', my_first_app_django),
]
