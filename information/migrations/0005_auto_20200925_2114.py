# Generated by Django 3.0.3 on 2020-09-25 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0004_auto_20200925_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='ware',
            name='wnum',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ware',
            name='whouse',
            field=models.ForeignKey(limit_choices_to={'hcategory': '货物存储'}, on_delete=django.db.models.deletion.CASCADE, to='information.Warehouse'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='hcategory',
            field=models.CharField(blank=True, choices=[('货物存储', '货物存储'), ('娱乐场所', '娱乐场所'), ('', '')], default=False, max_length=4),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='hname',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]