from django.contrib import admin

from calc.models import Calc


@admin.register(Calc)
class ConsultAdmin(admin.ModelAdmin):
    list_display = ('date_order', 'phone', 'fio', 'name_job', 'adress')