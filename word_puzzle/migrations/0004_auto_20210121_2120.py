# Generated by Django 3.0.3 on 2021-01-21 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word_puzzle', '0003_userprogress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprogress',
            name='solved_words',
            field=models.ManyToManyField(blank=True, to='word_puzzle.Word'),
        ),
    ]