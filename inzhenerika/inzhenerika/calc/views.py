from django.shortcuts import render
from calc.forms import CalcForm


def calc_form(request):
    calc_form = CalcForm()
    return render(request, template_name='calc.html', context={"calc_form": calc_form})