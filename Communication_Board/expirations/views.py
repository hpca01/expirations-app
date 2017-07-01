# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Drug, Expiration
from .forms import DrugForm, ExpirationForm

from django.urls import reverse_lazy, reverse

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

# Create your views here.

class DrugListView(ListView):
    context_object_name = 'drugs'
    model = Drug
    template_name = 'expirations/drug_list.html'

    def get_queryset(self):
        return Drug.objects.all().order_by('name')

class CreateDrugView(CreateView):
    redirect_field_name = reverse_lazy('drug_list')
    form_class = DrugForm

    model = Drug

class DrugDetailView(DetailView):
    template_name = 'expirations/drug_detail.html'
    model = Drug

    def get_context_data(self, **kwargs):
        drug_Pk = self.kwargs['pk']
        context = super(DrugDetailView, self).get_context_data(**kwargs)
        context['exp'] = Drug.objects.get(pk = drug_Pk).expiration_dates.all().order_by('expirationDate')
        return context

class DrugDeleteView(DeleteView):
    model = Drug
    success_url = reverse_lazy('drug_list')

class CreateExpirationView(CreateView):
    model = Expiration
    template_name = 'expirations/add_exp.html'
    form_class = ExpirationForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        exp = Expiration()
        exp.expirationDate = self.request.POST['expirationDate']
        exp.qty = self.request.POST['qty']
        exp.facility = self.request.POST['facility']
        #exp.comments = self.request.POST['comments']
        exp.drug_Linked = Drug.objects.get(pk = self.kwargs['pk'])
        exp.save()
        print(exp.expirationDate)
        return redirect('drug_detail', pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('drug_detail')

class ExpirationDeleteView(DeleteView):
    model = Expiration
    success_url = reverse_lazy('drug_list')
##funcs only

def home(request):
    return render(request, 'expirations/index.html')
