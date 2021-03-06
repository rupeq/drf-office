# Generated by Django 3.1.2 on 2020-10-10 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='№')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='№')),
                ('room_number', models.CharField(max_length=30, verbose_name='Room number')),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='officeapp.office')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='№')),
                ('seat_number', models.CharField(max_length=30, verbose_name='seat_number')),
                ('is_free', models.BooleanField(default=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='officeapp.room')),
            ],
        ),
    ]
