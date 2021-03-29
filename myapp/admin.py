from django.contrib import admin
from .models import Medicine
from .models import Sales
from .forms import MedCreateForm
class MedCreateAdmin(admin.ModelAdmin):
    list_display = ['name','company','exp_date','quantity']
    form=MedCreateForm
    list_filter = ['company']
    search_fields=['name','company']
admin.site.register(Sales)
admin.site.register(Medicine,MedCreateAdmin)