from currency.forms import BankForm, ContactUsForm

from django.views.generic import (CreateView, DeleteView, DetailView,
                                  ListView, UpdateView)


from currency.models import Banks, ContactUs, Rate  # noqa

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy


class BanksListView(ListView):
    template_name = 'bank_list.html'
    queryset = Banks.objects.all()


class BankDetailView(DetailView):
    template_name = 'bank_details.html'
    queryset = Banks.objects.all()


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


class BankCreateView(CreateView):
    template_name = 'bank_create.html'
    model = Banks
    form_class = BankForm

    success_url = reverse_lazy('currency:banks')


class BankUpdateView(UpdateView):
    queryset = Banks.objects.all()
    template_name = 'bank_update.html'
    success_url = reverse_lazy('currency:banks')
    model = Banks
    form_class = BankForm


# def bank_delete(request, pk):
#     instance = get_object_or_404(Banks, pk=pk)
#     instance.delete()
#     return redirect('currency:banks')


class BankDeleteView(DeleteView):
    queryset = Banks.objects.all()
    success_url = reverse_lazy('currency:banks')


class RateListView(ListView):
    template_name = 'rate_list.html'
    queryset = Rate.objects.all()


def index(request):
    return render(request, 'index.html')
