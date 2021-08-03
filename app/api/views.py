from api.filters import ContactUsFilter, RateFilter
from api.paginators import BanksPagination, ContactUsPagination, RatePagination
from api.serializers import BanksSerializer, ContactUsSerializer, RateSerializer
from api.throttles import AnonUserRateThrottle

from currency.models import Banks, ContactUs, Rate

from django.conf import settings
from django.core.mail import send_mail

from django_filters import rest_framework as filters

from rest_framework import filters as rest_framework_filters
from rest_framework import generics, viewsets
# from django.core.mail import EmailMessage


class BanksList(generics.ListAPIView):

    queryset = Banks.objects.all().prefetch_related('rate_set')
    serializer_class = BanksSerializer
    pagination_class = BanksPagination


# def send_email():
#     email = EmailMessage(
#         "from ContactUsViewSet",
#         data,
#         from,
#         [settings.DEFAULT_FROM_EMAIL],
#         fail_silently = False,
#     )
#     email.attach_file(ContactUsSerializer)
#     email.send()


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all().order_by('-created')
    serializer_class = ContactUsSerializer
    pagination_class = ContactUsPagination
    throttle_classes = [AnonUserRateThrottle]
    filterset_class = ContactUsFilter
    filter_backends = (filters.DjangoFilterBackend,
                       rest_framework_filters.OrderingFilter,
                       rest_framework_filters.SearchFilter,
                       )
    ordering_fields = ['id', 'email_from', 'subject', 'message', 'created']
    search_fields = ('id', 'email_from', 'subject', 'message',)

    # def create(self, request, *args, **kwargs):
    #     response = super(ContactUsViewSet, self).create(request, *args, **kwargs)
    #     send_email()
    #     return response

    def get_serializer_class(self):
        if 'create' in self.action:
            data = self.request._data

            send_mail(
                'data api creation',
                f'''
                generated data: (
                'subject': {data['subject']},
                'message': {data['message']},
                'email': {data['email_from']}
                )
                ''',
                settings.EMAIL_HOST_USER,
                [data['email_from']],
                fail_silently=False, )
        return ContactUsSerializer


class ContactUsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    pagination_class = RatePagination
    throttle_classes = [AnonUserRateThrottle]
    filterset_class = RateFilter
    filter_backends = (filters.DjangoFilterBackend,
                       rest_framework_filters.OrderingFilter,
                       rest_framework_filters.SearchFilter,
                       )
    ordering_fields = ['id', 'buy', 'sale', 'type', 'created']
    search_fields = ('id', 'buy', 'sale', 'type',)
