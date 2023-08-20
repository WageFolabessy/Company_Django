from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Company
from .forms import CompanyForm

class IndexView(ListView):
    model = Company
    template_name = 'Company/index.html'
    context_object_name = 'companies'

class CreateOrStoreView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'Company/add.html'
    success_url = reverse_lazy('company:index')

    def form_valid(self, form):
        messages.success(self.request, 'Company Created!')
        return super().form_valid(form)

class DetailView(DetailView):
    model = Company
    template_name = 'Company/detail.html'
    context_object_name = 'company'
    slug_field = 'name'
    slug_url_kwarg = 'name'

class EditOrUpdateView(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'Company/update.html'
    context_object_name = 'company'
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def get_success_url(self):
        messages.success(self.request, 'Company Updated!', extra_tags='success')
        return reverse_lazy('company:detail', kwargs={'name': self.object.name})

class DeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('company:index')
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def delete(self, request, *args, **kwargs):
        messages.success(request, f'Company {self.get_object().name} Deleted!')
        return super().delete(request, *args, **kwargs)
