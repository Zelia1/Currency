from django.http import HttpResponse
from django.shortcuts import render

from currency.models import Banks


def hello_world(request):
    return HttpResponse("Hello World")


def banks(request):
    queryset = Banks.objects.all()
    # list_banks = []
    # for bank in queryset:
    #     list_banks.append(bank.number_phone)

    context = {
        "message": "Hello World!",
    }
    return render(request, 'bank_list.html', context=context)
