# Generated by Django 4.2.7 on 2023-11-09 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Businessapp', '0002_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='color',
            field=models.CharField(default='white', max_length=50),
        ),
        migrations.AlterField(
            model_name='products',
            name='origin',
            field=models.CharField(default='Kenya', max_length=50),
        ),
    ]
