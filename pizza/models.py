from django.db import models

# Create your models here.

SIZE = ((None, 'Choose..'),
        ('small', 'Small'),
        ('Medium', 'Medium'),
        ('large', 'Large'),
)

PIZZA = (
        ('Neapolitan', 'Neapolitan'),
        ('Vegetarian', 'Vegetarian'),
        ('Margarita', 'Margarita'),
        ('Assorted', 'Assorted'),
)

SAUCE = (('Ketchup', 'Ketchup'),
        ('Mayonnaise', 'Mayonnaise'),
        ('Mustard', 'Mustard'),
        ('Chilli Sauce', 'Chilli Sauce'),
        ('Paprika Sauce', 'Paprika Sauce'),
)



class OrderModel(models.Model):
    size = models.CharField(choices=SIZE, blank=True, max_length=50)
    sauce = models.CharField(choices=SAUCE, max_length=50)
    pizza = models.CharField(choices=PIZZA, max_length=50)

    def __str__(self):
        return self.pizza