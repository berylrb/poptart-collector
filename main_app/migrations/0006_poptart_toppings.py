# Generated by Django 4.1 on 2022-08-08 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_topping'),
    ]

    operations = [
        migrations.AddField(
            model_name='poptart',
            name='toppings',
            field=models.ManyToManyField(to='main_app.topping'),
        ),
    ]