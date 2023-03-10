# Generated by Django 4.1.5 on 2023-02-01 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0004_announcement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField()),
                ('file', models.FileField(blank=True, null=True, upload_to='assignments/')),
                ('marks', models.DecimalField(decimal_places=2, max_digits=6)),
                ('course_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online.course')),
            ],
            options={
                'verbose_name_plural': 'Assignments',
                'ordering': ['-datetime'],
            },
        ),
    ]
