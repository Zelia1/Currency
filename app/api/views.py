from rest_framework import generics, viewsets
from currency.models import Banks, ContactUs
from api.serializers import BanksSerializer, ContactUsSerializer
from api.paginators import BanksPagination


class BanksList(generics.ListAPIView):
    queryset = Banks.objects.all()
    serializer_class = BanksSerializer
    pagination_class = BanksPagination


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

    def get_serializer_class(self):
        # if 'create' in self.action:
        #     pass
        return ContactUsSerializer


class ContactUsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
