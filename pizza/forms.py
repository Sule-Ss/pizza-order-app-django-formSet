
from django import forms
from .models import OrderModel

class PizzaForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields= ['size', 'pizza', 'sauce']
        labels = {
            'size' : 'Size',
            'pizza' : 'Pizza',
            'sauce' : 'Extra Sauces',
        }

        widgets = {
            'sauce' : forms.CheckboxSelectMultiple(),
            'pizza' : forms.RadioSelect()
        }