from rest_framework import serializers
from currency.models import Banks, ContactUs


class BanksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banks
        fields = (
            'id',
            'name',
            'url',
            'email_from',
            'number_phone',
            'created'
        )


class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = (
            'id',
            'email_from',
            'subject',
            'message',
            'created'
        )
