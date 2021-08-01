from rest_framework import serializers
from currency.models import Banks, ContactUs, Rate


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = (
            'id',
            'name',
            'sale',
            'buy',
            'type'
        )


class BanksSerializer(serializers.ModelSerializer):
    # rate = RateSerializer()

    class Meta:
        model = Banks
        fields = (
            'id',
            'name',
            'url',
            'email_from',
            'number_phone',
            'created'
            # 'rate'
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


