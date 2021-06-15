from currency.forms import BankForm, ContactUsForm

from currency.models import Banks, ContactUs  # noqa

from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render, reverse, redirect


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


def contactus_details(request, pk):
    instance = get_object_or_404(ContactUs, pk=pk)

    context = {
        "object": instance
    }

    return render(request, 'contactus_details.html', context=context)


def contactus_create(request):
    if request.method == 'POST':
        form_data = request.POST
        form = ContactUsForm(form_data)
        if form.is_valid():
            form.save()
            return redirect('currency:contactus-list')
    elif request.method == 'GET':
        form = ContactUsForm()
    context = {
        'message': "Contact create",
        'form': form,
    }
    return render(request, 'contactus_create.html', context=context)


def contactus_update(request, pk):
    instance = get_object_or_404(ContactUs, pk=pk)
    if request.method == 'POST':
        form_data = request.POST
        form = ContactUsForm(form_data, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('currency:contactus-list')
    elif request.method == 'GET':
        form = ContactUsForm(instance=instance)
    context = {
        'message': "Contact update",
        'form': form,
    }
    return render(request, 'contactus_update.html', context=context)


def contact_delete(request, pk):
    instance = get_object_or_404(ContactUs, pk=pk)
    instance.delete()
    return redirect('currency:contactus-list')


def bank_create(request):
    if request.method == 'POST':
        form_data = request.POST
        form = BankForm(form_data)
        if form.is_valid():
            form.save()
            return redirect('currency:banks')
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
            return redirect('currency:banks')
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
    return redirect('currency:banks')


def index(request):
    return render(request, 'index.html')
