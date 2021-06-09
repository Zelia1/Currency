from currency.models import Banks, ContactUs

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render


def hello_world(request):
    return HttpResponse("Hello World")


def banks(request):
    queryset = Banks.objects.all()

    context = {
        "objects": queryset,
    }
    return render(request, 'bank_list.html', context=context)


def bank_details(request, pk):
    bank = get_object_or_404(Banks, pk=pk)

    context = {
        "object": bank
    }
    return render(request, 'bank_details.html', context=context)


def contactus_list(request):
    queryset = ContactUs.objects.all()

    context = {
        "objects": queryset,
    }
    return render(request, 'contactus_list.html', context=context)
