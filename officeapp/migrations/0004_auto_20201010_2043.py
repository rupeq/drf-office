# Generated by Django 3.1.2 on 2020-10-10 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officeapp', '0003_auto_20201010_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
