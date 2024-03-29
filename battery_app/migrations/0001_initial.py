# Generated by Django 5.0.2 on 2024-03-13 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BatteryData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_file', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='CellInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('cell_type', models.CharField(max_length=100)),
                ('form_factor', models.CharField(max_length=100)),
                ('mass', models.FloatField()),
                ('height', models.FloatField()),
                ('diameter', models.FloatField()),
                ('volume', models.FloatField()),
            ],
        ),
    ]
