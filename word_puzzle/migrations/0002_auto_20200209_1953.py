# Generated by Django 3.0.3 on 2020-02-09 16:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word_puzzle', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='location',
        ),
        migrations.AddField(
            model_name='word',
            name='order',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='word',
            name='word',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='word',
            name='x_start',
            field=models.IntegerField(default=999, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='word',
            name='y_start',
            field=models.IntegerField(default=999, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
    ]
