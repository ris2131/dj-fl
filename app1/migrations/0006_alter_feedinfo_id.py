# Generated by Django 3.2.6 on 2021-09-08 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20210908_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedinfo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]