
from .models import Pizza, Sauce
from django import forms


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = "__all__"



class SauceForm(forms.ModelForm):
    class Meta:
        model = Sauce
        # fields = "__all__"
        exclude = ("pizza",)

    widgets = {
        'sauce' : forms.CheckboxSelectMultiple()
            
        }
    







# class PizzaForm(forms.ModelForm):
#     class Meta:
#         model = OrderModel
#         fields= ['size', 'pizza', 'sauce']
#         labels = {
#             'size' : 'Size',
#             'pizza' : 'Pizza',
#             'sauce' : 'Extra Sauces',
#         }

#         widgets = {
#             'sauce' : forms.CheckboxSelectMultiple(),
#             'pizza' : forms.RadioSelect()
#         }