from currency.views import hello_world

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('first-app/', hello_world),
]
