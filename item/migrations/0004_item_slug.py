# Generated by Django 2.2.4 on 2019-08-08 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_auto_20190808_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]