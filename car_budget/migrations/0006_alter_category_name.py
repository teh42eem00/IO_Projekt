# Generated by Django 3.2.13 on 2022-06-09 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_budget', '0005_alter_car_budget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('1', 'Service'), ('2', 'Fuel'), ('3', 'Expense')], max_length=1),
        ),
    ]
