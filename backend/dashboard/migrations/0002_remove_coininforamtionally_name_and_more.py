# Generated by Django 4.1.2 on 2022-10-27 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coininforamtionally',
            name='name',
        ),
        migrations.RemoveField(
            model_name='stockinformationally',
            name='name',
        ),
        migrations.AddField(
            model_name='coininforamtionally',
            name='e_name',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='coininforamtionally',
            name='k_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='coininforamtionally',
            name='market_name',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='datainjection',
            name='e_name',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='datainjection',
            name='market_name',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='realstateinformationlly',
            name='e_name',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='realstateinformationlly',
            name='market_name',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='stockinformationally',
            name='e_name',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='stockinformationally',
            name='k_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='stockinformationally',
            name='market_name',
            field=models.CharField(default='', max_length=10),
        ),
    ]
