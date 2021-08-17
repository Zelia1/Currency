from currency.forms import BankForm, ContactUsForm, RateForm
from currency.models import Banks, ContactUs, Rate  # noqa
from currency.tasks import send_email_contactus
from currency.filters import RateFilter
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  ListView, UpdateView, )
from django_filters.views import FilterView


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
        send_email_contactus.delay(body)

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


class RateListView(FilterView):
    template_name = 'rate_list.html'
    queryset = Rate.objects.all().select_related('bank')
    paginate_by = 25
    filterset_class = RateFilter


class RateUpdateView(UpdateView):
    queryset = Rate.objects.all()
    template_name = 'rate_update.html'
    success_url = reverse_lazy('currency:rate-list')
    model = Rate
    form_class = RateForm


class RateDetailView(DetailView):
    template_name = 'rate_details.html'
    queryset = Rate.objects.all()


class RateDeleteView(DeleteView):
    template_name = 'rate_confirm_delete.html'
    queryset = Rate.objects.all()
    success_url = reverse_lazy('currency:rate-list')


class RateCreateView(CreateView):
    template_name = 'rate_create.html'
    model = Rate
    form_class = RateForm

    success_url = reverse_lazy('currency:rate-list')


# class RateDeleteView(UserPassesTestMixin, DeleteView):
#     template_name = 'rate_confirm_delete.html'
#     queryset = Rate.objects.all()
#     success_url = reverse_lazy('currency:rate-list')
#
#     def superuser_validity_check(self):
#         self.queryset = self.get_object()
#         return self.request.user.is_superuser

def index(request):
    return render(request, 'index.html')
