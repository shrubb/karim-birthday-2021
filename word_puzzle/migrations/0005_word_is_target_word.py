# Generated by Django 3.0.3 on 2021-01-21 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word_puzzle', '0004_auto_20210121_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='is_target_word',
            field=models.BooleanField(default=True),
        ),
    ]
