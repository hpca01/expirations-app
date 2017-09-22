from django import forms
from .models import Drug, Expiration, Barcode

class DrugForm(forms.ModelForm):

    class Meta:
        model = Drug
        fields = ('name',)


class ExpirationForm(forms.ModelForm):
    facility = forms.ChoiceField(choices = Expiration.facility_Choices)
    class Meta:
        model = Expiration
        fields = ('qty', 'facility','expirationDate',)


class BarcodeForm(forms.ModelForm):
    class Meta:
        model = Barcode
        fields = ('barCode',)
