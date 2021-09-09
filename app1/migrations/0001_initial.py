# Generated by Django 3.2.6 on 2021-09-09 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feedInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(default='no brand data', max_length=20)),
                ('name', models.CharField(default='no feedName data', max_length=40)),
                ('foodType', models.CharField(default='no info', max_length=10)),
                ('size', models.CharField(default='no size data', max_length=10)),
                ('flavor', models.CharField(default='no Flavor data', max_length=40)),
                ('alg', models.CharField(default='no allergy data', max_length=40)),
                ('health', models.CharField(default='no health data', max_length=20)),
                ('explain', models.CharField(default='no explain data', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='guest', max_length=20)),
                ('pw', models.CharField(default='abcdefgh', max_length=20)),
            ],
        ),
    ]
