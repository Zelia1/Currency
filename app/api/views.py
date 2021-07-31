from rest_framework import generics, viewsets
from currency.models import Banks, ContactUs
from api.serializers import BanksSerializer, ContactUsSerializer
from api.paginators import BanksPagination
# from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings


class BanksList(generics.ListAPIView):
    queryset = Banks.objects.all()
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
