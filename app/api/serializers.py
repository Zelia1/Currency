from currency.models import Banks, ContactUs, Rate

from rest_framework import serializers


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = (
            'id',
            'sale',
            'buy',
        )


class BanksSerializer(serializers.ModelSerializer):
    rate_set = RateSerializer(many=True)

    class Meta:
        model = Banks
        fields = (
            'id',
            'name',
            'url',
            'email_from',
            'number_phone',
            'created',
            'rate_set'
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
