from currency.views import (index)
from api.views import BanksList
    # ContactUsList, ContactUsDetails

import debug_toolbar

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/banks', BanksList.as_view(), ),
    path('api/', include('api.urls')),

    path('', index, name='index'),
    path('auth/', include('django.contrib.auth.urls')),
    path('currency/', include('currency.urls')),
    path('accounts/', include('accounts.urls')),
    path('__debug__/', include(debug_toolbar.urls)),

]

urlpatterns.extend(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
