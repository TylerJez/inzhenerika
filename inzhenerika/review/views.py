from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from . import forms
from .forms import ReviewForm
from .models import Review
from django.views.generic.base import View
def review(request):
    review_form = ReviewForm()
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            reviews = Review()
            reviews.score = review_form.cleaned_data['score']
            reviews.fio = review_form.cleaned_data['fio']
            reviews.comment = review_form.cleaned_data['comment']
            reviews.save()
    return render(request, template_name='feedback-form.html', context={"review_form": review_form})
def notify_review(request):
    review_form = ReviewForm()
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = Review()
            review.score = review_form.cleaned_data['score']
            review.fio = review_form.cleaned_data['fio']
            review.comment = review_form.cleaned_data['comment']
            review.save()
    return render(request, template_name='feedback-notify.html', context={"review_form": review_form})
class ReviewView(View):
    def get(self, request):
        review_list = Review.objects.all()
        return render(request, template_name='feedback.html', context={'review_list': review_list})