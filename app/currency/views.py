from currency.models import Banks, ContactUs

from currency.forms import BankForm

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect


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


def bank_create(request):
    
    if request.method == 'POST':
        form_data = request.POST
        form = BankForm(form_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/banks/')
    elif request.method == 'GET':
        form = BankForm()
    
    context = {
        'message': "Bank create",
        'form': form,
    }
    return render(request, 'bank_create.html', context=context)


def bank_update(request, pk):
    instance = get_object_or_404(Banks, pk=pk)
    
    if request.method == 'POST':
        form_data = request.POST
        form = BankForm(form_data, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/banks/')
    elif request.method == 'GET':
        form = BankForm(instance=instance)

    context = {
        'message': "Bank update",
        'form': form,
    }
    return render(request, 'bank_update.html', context=context)


def bank_delete(request, pk):
    instance = get_object_or_404(Banks, pk=pk)
    instance.delete()
    return HttpResponseRedirect('/currency/banks/')
    

    return render(request, 'bank_delete.html', context=context)