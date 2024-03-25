from django import forms

class CalcForm(forms.Form):
    name_job = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'input-name', 'placeholder': 'Название работ (квартира до 100 кв.м)'}
        ),
        label=''
        )
    fio = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'input-name', 'placeholder': 'Ваше ФИО'}
        ),
        label=''
        )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'input-name', 'placeholder': 'Ваш телефон'}
        ),
        label=''
        )
    adress = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'input-name', 'placeholder': 'Ваш адрес'}
        ),
        label=''
        )