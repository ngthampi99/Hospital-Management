# Generated by Django 4.2.1 on 2023-09-12 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registerdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email_ID', models.EmailField(blank=True, max_length=254, null=True)),
                ('Mob_No', models.IntegerField(blank=True, null=True)),
                ('Password', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]