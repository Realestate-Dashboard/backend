# Generated by Django 4.1.2 on 2022-10-27 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_remove_coininforamtionally_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coininforamtionally',
            name='end_price',
        ),
        migrations.RemoveField(
            model_name='coininforamtionally',
            name='price',
        ),
        migrations.RemoveField(
            model_name='coininforamtionally',
            name='start_price',
        ),
        migrations.RemoveField(
            model_name='datainjection',
            name='e_name',
        ),
        migrations.RemoveField(
            model_name='datainjection',
            name='market_name',
        ),
        migrations.RemoveField(
            model_name='realstateinformationlly',
            name='e_name',
        ),
        migrations.RemoveField(
            model_name='realstateinformationlly',
            name='market_name',
        ),
        migrations.RemoveField(
            model_name='stockinformationally',
            name='end_price',
        ),
        migrations.RemoveField(
            model_name='stockinformationally',
            name='price',
        ),
        migrations.RemoveField(
            model_name='stockinformationally',
            name='start_price',
        ),
    ]