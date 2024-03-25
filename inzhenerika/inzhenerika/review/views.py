from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from . import forms
from .forms import ReviewForm
from .models import Review
from django.views.generic.base import View


class ReviewView(View):
    def get(self, request):
        review_list = Review.objects.all()
        return render(request, template_name='feedback.html', context={'review_list': review_list})

def review(request):
    review_form = ReviewForm()
    return render(request, template_name='feedback.html', context={"review_form": review_form})


def review_send(request):
    if request.method == "POST":
        review: Review = Review()
        review.score=ReviewForm.POST.get("score")
        review.fio=ReviewForm.POST.get("fio")
        review.comment=ReviewForm.POST.get("comment")
        review.save()
    return HttpResponseRedirect("/")


'''def review_send(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            instance = review_form.save(commit=False)
            instance.save()
            return redirect('index')
        else:
            review_form = ReviewForm()
        return render(request, template_name='feedback.html', context={"review_form": review_form})'''
