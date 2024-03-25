from django.contrib import admin
from .models import Consult

@admin.register(Consult)
class ConsultAdmin(admin.ModelAdmin):
    list_display = ('date_consult', 'phone', 'fio')