from django.contrib import admin
from .models import Medicine
from .models import Sales
from .forms import MedCreateForm
from import_export.admin import ImportExportModelAdmin

@admin.register(Medicine,Sales)
class ViewAdmin(ImportExportModelAdmin):
    pass
