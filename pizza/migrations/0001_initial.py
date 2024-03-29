# Generated by Django 4.0.5 on 2022-06-15 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[(None, 'Choose..'), ('small', 'Small'), ('Medium', 'Medium'), ('large', 'Large')], max_length=50)),
                ('cesit', models.CharField(choices=[('Neapolitan', 'Neapolitan'), ('Vegetarian', 'Vegetarian'), ('Margarita', 'Margarita'), ('Assorted', 'Assorted')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sauce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ketchup', models.BooleanField(default=False)),
                ('Mayonnaise', models.BooleanField(default=False)),
                ('Mustard', models.BooleanField(default=False)),
                ('ChilliSauce', models.BooleanField(default=False)),
                ('PaprikaSauce', models.BooleanField(default=False)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sauces', to='pizza.pizza')),
            ],
        ),
    ]
