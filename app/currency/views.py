from currency.forms import BankForm, ContactUsForm

from django.views.generic import (CreateView, DeleteView, DetailView,
                                  ListView, UpdateView)


from currency.models import Banks, ContactUs, Rate  # noqa

from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy


class BanksListView(ListView):
    template_name = 'bank_list.html'
    queryset = Banks.objects.all()


class BankDetailView(DetailView):
    template_name = 'bank_details.html'
    queryset = Banks.objects.all()


class ContactUsListView(ListView):
    template_name = 'contactus_list.html'
    queryset = ContactUs.objects.all()


class ContactusDetailView(DetailView):
    template_name = 'contactus_details.html'
    queryset = ContactUs.objects.all()


class ContactUsCreateView(CreateView):
    template_name = 'contactus_create.html'
    model = ContactUs
    form_class = ContactUsForm

    success_url = reverse_lazy('currency:contactus-list')

    def form_valid(self, form):
        data = form.cleaned_data
        body = f'''
        From: {data['email_from']}
        Topic: {data['subject']}
        \n
        Message: {data['message']}
        '''
        send_mail(
            'Hello from contactus!',
            body,
            'PavelTest1990@gmail.com',
            ['zelenskiy.zelia@gmail.com'],
            fail_silently=False,
        )
        return super().form_valid(form)


class ContactUsUpdateView(UpdateView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_update.html'
    success_url = reverse_lazy('currency:contactus-list')
    model = ContactUs
    form_class = ContactUsForm


class ContactDeleteView(DeleteView):
    template_name = 'contact_confirm_delete.html'
    queryset = ContactUs.objects.all()
    success_url = reverse_lazy('currency:contactus-list')


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


class BankDeleteView(DeleteView):
    template_name = 'bank_confirm_delete.html'
    queryset = Banks.objects.all()
    success_url = reverse_lazy('currency:banks')


class RateListView(ListView):
    template_name = 'rate_list.html'
    queryset = Rate.objects.all()


def index(request):
    return render(request, 'index.html')
