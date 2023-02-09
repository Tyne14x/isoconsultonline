# Generated by Django 4.1.3 on 2023-01-04 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=50)),
                ('cusemail', models.CharField(max_length=100)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
