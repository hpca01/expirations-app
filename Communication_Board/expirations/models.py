# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
import datetime
from django.db import models
from django.db.models import Min

# Create your models here.

class Drug(models.Model):
    #drug_barcode = models.ForeignKey('expirations.Barcode', related_nam='barcodes')
    name = models.CharField(max_length= 200)

    # def get_absolute_url(self):
    #     return reverse('drug_list')

    def __unicode__(self):
        return self.name

    def early_exp(self):
        return self.expiration_dates.all().aggregate(Min('expirationDate')).values()[0]


class Expiration(models.Model):

    facility_Choices = (
        ('RWC', 'Redwood City Inpatient'),
        ('SC', 'Santa Clara Inpatient'),
        ('SLN', 'San Leandro Inpatient'),
    )

    facility = models.CharField(max_length = 100, choices = facility_Choices, default = 'RWC')

    drug_Linked = models.ForeignKey('expirations.Drug', related_name = 'expiration_dates')

    qty = models.IntegerField(default = 1)
    date_entered = models.DateField(auto_now=True)
    expirationDate = models.DateField(default = datetime.date.today)
    comments = models.TextField(null = True)

    def __unicode__(self):
        return str(self.expirationDate)

    def quantity(self):
        return int(self.quantity)

    def return_facility(self):
        return str(self.facility)

class Barcode(models.Model):
    drug = models.ForeignKey('expirations.Drug', related_name = 'barcode_for_drug')
    barCode = models.CharField(max_length= 40)

    def __unicode__(self):
        return str(self.barCode)
