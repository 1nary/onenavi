# Generated by Django 2.2.28 on 2022-12-23 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='income',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]