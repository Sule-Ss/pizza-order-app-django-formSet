from django.shortcuts import redirect, render

from pizza.forms import PizzaForm

# Create your views here.

def home(request):
    return render(request, 'pizza/home.html')

def orderView(request):
    form = PizzaForm()
    if request.method == 'POST':
        form = PizzaForm(request.POST, many=True)
        if form.is_valid():
            pizza_order = form.save(commit=False)
            pizza_order.save()
            return redirect('home')

    # print('form',form)
    context ={
        'form':form
    }
    return render(request, 'pizza/order.html', context)