from django.shortcuts import render

from calc.forms import CalcForm
from calc.models import Calc


def get(self, request):
    calc_list = Calc.objects.all()
    return render(request, template_name='calc.html', context={'calc_list': calc_list})

def calc(request):
    calc_form = CalcForm()
    if request.method == "POST":
        calc = Calc()
        calc.fio = request.POST.get("fio")
        calc.phone = request.POST.get("phone")
        calc.name_job = request.POST.get("name_job")
        calc.adress = request.POST.get("adress")
        calc.save()
    return render(request, template_name='calc.html', context={'calc_form': calc_form})

def notify_calc(request):
    calc_form = CalcForm()
    if request.method == "POST":
        calc = Calc()
        calc.fio = request.POST.get("fio")
        calc.phone = request.POST.get("phone")
        calc.name_job = request.POST.get("name_job")
        calc.adress = request.POST.get("adress")
        calc.save()
    return render(request, template_name='zayavka-notify.html')