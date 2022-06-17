
from django.urls import path
from .views import home, numberOfPizza, order, addPizza

urlpatterns = [
    path("", home, name="home"),
    path("order/", order, name="order"),
    path("pizzas/", numberOfPizza, name="pizzas"),
    path("addPizza/", addPizza, name="addPizza"),

]