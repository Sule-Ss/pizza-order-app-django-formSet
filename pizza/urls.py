from django.urls import path
from .views import home, orderView

urlpatterns = [
    path('', home, name="home"),
    path('order/', orderView, name="order")
]