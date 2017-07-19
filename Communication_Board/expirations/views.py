# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from django.template import Context

from django.http import JsonResponse

from .models import Drug, Expiration, Barcode
from .forms import DrugForm, ExpirationForm, BarcodeForm

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

class DrugExpListView(ListView):
    context_object_name = 'drugs_exp'
    model = Drug
    template_name = 'expirations/drug_list_byEXP.html'

    def get_queryset(self):
        return Expiration.objects.all().order_by('expirationDate')

class AjaxableResponseMixin(object):
    def form_valid(self, form):
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            object_rtn = Drug.objects.get(pk = self.object.pk)
            data = {
                'name': self.object.name,
                }
            return JsonResponse(data)
        else:
            return response
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

class CreateDrugView(AjaxableResponseMixin, CreateView):
    redirect_field_name = reverse_lazy('drug_list')
    form_class = DrugForm

    model = Drug

    def get_success_url(self):
        return reverse_lazy('drug_new')

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
        exp.expirationDate = form.cleaned_data['expirationDate']
        exp.qty = form.cleaned_data['qty']
        exp.facility = form.cleaned_data['facility']
        #exp.comments = self.request.POST['comments']
        exp.drug_Linked = Drug.objects.get(pk = self.kwargs['pk'])
        exp.save()
        return redirect('drug_detail', pk=self.kwargs['pk'])

    def get_context_data(self):
        drug_pk = self.kwargs['pk']
        context = {"drug_name" : Drug.objects.get(pk = drug_pk), 'form':self.get_form()}
        return context

    def get_success_url(self):
        return reverse_lazy('drug_detail')

class ExpirationDeleteView(DeleteView):
    model = Expiration
    success_url = reverse_lazy('drug_list')
##funcs only


class CreateBarcodeView(CreateView):
    model = Barcode
    template_name = 'expirations/add_barcode.html'
    form_class = BarcodeForm

    def form_valid(self, form):
        self.object = form.save(commit = False)
        barcode = Barcode()
        barcode.barCode = form.cleaned_data['barCode']
        barcode.drug = Drug.objects.get(pk = self.kwargs ['pk'])
        barcode.save()
        return redirect('drug_detail', pk = self.kwargs['pk'])

    def get_context_data(self):
        drug_pk = self.kwargs['pk']
        context = {"drug_name": Drug.objects.get(pk = drug_pk), 'form':self.get_form()}
        return context


def home(request):
    return render(request, 'expirations/index.html')
