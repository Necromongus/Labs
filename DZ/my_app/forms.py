from django import forms
from my_app.models import *


class CardForm(forms.ModelForm):
    class Meta:
        model = Vcard
        fields = ["id_card", "card_creator", "card_name", "photo", "card_price"]
        #widgets = {'information': forms.Textarea(attrs={'resize': 'none'})}

class HumanForm(forms.ModelForm):
    class Meta:
        model = Human
        fields = ["id_human", "fio", "order_code"]
        #widgets = {'information': forms.Textarea(attrs={'resize': 'none'})}
