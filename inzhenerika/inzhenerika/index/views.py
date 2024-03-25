from django.shortcuts import render
from index.forms import ConsultForm
from index.models import Consult


def index(request):
    return render(request, template_name='index.html')


def consult(request):
    consult_form = ConsultForm()
    if request.method == "POST":
        consult = Consult()
        consult.fio = request.POST.get("fio")
        consult.phone = request.POST.get("phone")
        consult.comment = request.POST.get("comment")
        consult.save()
    return render(request, template_name='index.html', context={'consult_form': consult_form})
