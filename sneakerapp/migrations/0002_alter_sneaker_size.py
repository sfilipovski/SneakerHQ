# Generated by Django 4.2.2 on 2023-08-30 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneakerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sneaker',
            name='size',
            field=models.CharField(choices=[('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46')], max_length=20),
        ),
    ]
