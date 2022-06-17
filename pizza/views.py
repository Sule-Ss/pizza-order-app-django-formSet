from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import PizzaForm, SauceForm
from django.forms import modelformset_factory, inlineformset_factory
from .models import Pizza, Sauce

# Create your views here.


def home(request):
    return render(request, "pizza/home.html")



def order(request):
    form = PizzaForm()

    context = {
        "form" : form
    }

    return render(request, "pizza/order.html", context)






def numberOfPizza(request):
    number_pizza = int(request.GET.get("number"))
    PizzaFormSet= modelformset_factory(Pizza, fields=('__all__'), extra=number_pizza  )
    SauceFormSet= modelformset_factory(Sauce, fields=( 'Ketchup', 'Mayonnaise', 'Mustard', 'ChilliSauce', 'PaprikaSauce'), extra=number_pizza  )
    
    if request.method == "POST":
        pizzaFormSet = PizzaFormSet(request.POST )
        sauceFormset =SauceFormSet(request.POST )

        print("asdasdadasdsssssssssssssssssssssssssssssssssssssssssssss")

        if pizzaFormSet.is_valid and sauceFormset.is_valid():
            print("asdasdadasdsssssssssssssssssssssssssssssssssssssssssssss")
            pizzas= pizzaFormSet.save()
            sauces= sauceFormset.save(commit=False)
            
            for i, sauce in enumerate(sauces):
                print(pizzas[i] )
                sauce.pizza = pizzas[i]
                sauce.save()

            # pizza = pizzaForm.save()
            # sauce = sauceForm.save(commit = False)
            # sauce.pizza = pizza 
            # sauce.save()
            return redirect("home")
    else:
        pizzaFormSet = PizzaFormSet(queryset = Pizza.objects.none())
        # sauceFormset = SauceFormSet()            
        sauceFormSet = SauceFormSet(queryset = Sauce.objects.none() )
        
        

    context = {
        "pizzaFormSet" : pizzaFormSet,
        'sauceFormSet': sauceFormSet,
    }

    return render(request, "pizza/pizzas.html", context)


def addPizza(request):

    if request.method == "POST":
        pizzaForm = PizzaForm(request.POST)
        sauceForm = SauceForm(request.POST)
        if pizzaForm.is_valid() and sauceForm.is_valid():
            pizza = pizzaForm.save()
            sauce = sauceForm.save(commit = False)
            sauce.pizza = pizza 
            sauce.save()
            return redirect("home")
