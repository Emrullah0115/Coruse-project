# Generated by Django 4.2.4 on 2023-08-19 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('imageUrl', models.CharField(blank=True, max_length=50)),
                ('date', models.DateField()),
                ('isActive', models.BooleanField()),
            ],
        ),
    ]
