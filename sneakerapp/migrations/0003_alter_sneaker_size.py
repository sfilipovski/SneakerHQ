# Generated by Django 4.2.2 on 2023-08-30 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneakerapp', '0002_alter_sneaker_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sneaker',
            name='size',
            field=models.CharField(max_length=200),
        ),
    ]