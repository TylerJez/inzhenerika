from django import forms


class CalcForm(forms.Form):
    name_job = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'input-name', 'placeholder': 'Название работ (квартира до 100 м^2)', 'type': 'text'}
        ),
        label=''
    )
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
    adress = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'input-name', 'placeholder': 'Ваш адрес', 'type': 'text'}
        ),
        label=''
    )