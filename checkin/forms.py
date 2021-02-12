from django import forms
from .models import Tenant

# register form
class TenantForm(forms.ModelForm):
    id_no = forms.IntegerField(required=False)
    temperature = forms.DecimalField(max_value=100,min_value=10)
    class Meta:
        model =Tenant
        fields = ['name','id_no', 'telephone','company']
    