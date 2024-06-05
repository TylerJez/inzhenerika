from django import forms


class ConsultForm(forms.Form):
    fio = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'input-name', 'placeholder': 'Ваше ФИО', 'type': 'text'}
        ),
        label=''
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'input-name', 'placeholder': 'Ваш телефон', 'type': 'text'}
        ),
        label=''
    )
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'comment', 'placeholder': 'Подробное описание причины', 'type': 'text'}
        ),
        label=''
    )