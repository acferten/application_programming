# Generated by Django 4.1.7 on 2023-03-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=13, max_digits=15)),
                ('longitude', models.DecimalField(decimal_places=13, max_digits=15)),
            ],
        ),
    ]
