# Generated by Django 2.2.15 on 2020-10-01 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_eventpage_meetup_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descripción'),
        ),
    ]
