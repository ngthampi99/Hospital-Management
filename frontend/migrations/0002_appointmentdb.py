# Generated by Django 4.2.1 on 2023-09-13 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointmentdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department', models.CharField(blank=True, max_length=100, null=True)),
                ('Doctor', models.CharField(blank=True, max_length=100, null=True)),
                ('DOB', models.IntegerField(blank=True, null=True)),
                ('Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('Message', models.TextField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
