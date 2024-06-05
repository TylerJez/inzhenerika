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
    score = forms.ChoiceField(
        choices=SCORE,
        widget=forms.Select(
            attrs={"class": "score-section"}
        ),
        label='Ваша оценка:',
        label_suffix="<label class='score'><span>Ваша оценка:</span></label>"

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