# Generated by Django 3.0.3 on 2020-10-01 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0020_visitorflow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitorflow',
            name='Vdate',
            field=models.DateField(),
        ),
    ]