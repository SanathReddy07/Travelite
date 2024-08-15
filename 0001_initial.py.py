# Generated by Django 2.0.4 on 2018-05-07 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(default='Stony Brook', max_length=30)),
                ('attractionName', models.CharField(max_length=30)),
                ('attractionDescription', models.CharField(max_length=1000)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=30)),
                ('sourceLocation', models.CharField(max_length=30)),
                ('destinationLocation', models.CharField(max_length=30)),
                ('departureDate', models.DateField()),
                ('departureTime', models.TimeField()),
                ('fareEconomy', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fareBusiness', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fareFirst', models.DecimalField(decimal_places=2, max_digits=6)),
                ('numSeatsRemainingEconomy', models.IntegerField()),
                ('numSeatsRemainingBusiness', models.IntegerField()),
                ('numSeatsRemainingFirst', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userEmail', models.CharField(max_length=36)),
                ('bookingType', models.CharField(choices=[('flight', 'Flight'), ('train', 'Train'), ('hotel', 'Hotel')], max_length=6)),
                ('bookingStartDate', models.DateField()),
                ('paymentAmount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('paymentCardNo', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField()),
                ('dailyCost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=2)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('paymentType', models.CharField(choices=[('credit', 'Credit'), ('debit', 'Debit')], max_length=6)),
                ('cardNo', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=30)),
                ('sourceLocation', models.CharField(max_length=30)),
                ('destinationLocation', models.CharField(max_length=30)),
                ('departureDate', models.DateField()),
                ('departureTime', models.TimeField()),
                ('fareEconomy', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fareBusiness', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fareFirst', models.DecimalField(decimal_places=2, max_digits=6)),
                ('numSeatsRemainingEconomy', models.IntegerField()),
                ('numSeatsRemainingBusiness', models.IntegerField()),
                ('numSeatsRemainingFirst', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=35, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]