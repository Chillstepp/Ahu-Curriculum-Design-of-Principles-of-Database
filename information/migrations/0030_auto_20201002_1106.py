# Generated by Django 3.0.3 on 2020-10-02 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20200924_2110'),
        ('information', '0029_auto_20201002_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managerhouse',
            name='house',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='information.Warehouse'),
        ),
        migrations.AlterField(
            model_name='managerhouse',
            name='manager',
            field=models.OneToOneField(default=6, on_delete=django.db.models.deletion.CASCADE, to='login.Manager'),
        ),
    ]