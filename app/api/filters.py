from django_filters import rest_framework as filters
from currency.models import ContactUs


class ContactUsFilter(filters.FilterSet):

    class Meta:
        model = ContactUs
        fields = {
            'email_from': ('icontains', 'istartswith', 'iendswith', 'exact'),
            'subject': ('icontains', 'istartswith', 'iendswith', 'exact'),
            'message': ('icontains', 'istartswith', 'iendswith', 'exact'),
            'created': ('date', 'lte', 'gte', 'range'),
        }
