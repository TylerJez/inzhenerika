from django import forms
from django.shortcuts import redirect, render

SCORE = [
    (5, 5),
    (4, 4),
    (3, 3),
    (2, 2),
    (1, 1),
]

class ReviewForm(forms.Form):
    score = forms.CharField(
        widget=forms.Select(
            choices=SCORE,
            attrs={"class": "score-section"}
        ),
        label=''

    )
    fio = forms.CharField(
        min_length=3,
        widget=forms.TextInput(
            attrs={'class': 'input-name', 'placeholder': 'Ваше ФИО'}
        ),
        label=''
    )
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'comment', 'placeholder': 'Комментарий', 'cols': 30, 'rows': 10}
        ),
        label=''
    )
