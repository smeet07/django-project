from django import forms
from .models import Medicine,Sales
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
class MedCreateForm(forms.ModelForm):
    class Meta:
        model= Medicine
        fields=['name','company','exp_date','quantity','price']
    def clean_name(self):
        name=self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This filed is required')
        return name
    def clean_company(self):
        company=self.cleaned_data.get('company')
        if not company:
            raise forms.ValidationError('This filed is required')
        return company
class MedSearchForm(forms.ModelForm):
    export_to_csv=forms.BooleanField(required=False)
    class Meta:
        model=Medicine
        fields=['name','company']
class MedUpdateForm(forms.ModelForm):
    class Meta:
        model=Medicine
        fields=['name','company','exp_date','quantity','price']
class SellForm(forms.ModelForm):
    class Meta:
        model=Medicine
        fields=['sell_quantity']
class PurchaseForm(forms.ModelForm):
    class Meta:
        model=Medicine
        fields=['purchase_quantity']
class reorder(forms.ModelForm):
    class Meta:
        model=Medicine
        fields=['reorder_level']
class CreateBillForm(forms.ModelForm):
    class Meta:
        model=Sales
        fields=['name','company','Sales_date','quantity','amount']
