# Generated by Django 4.2.2 on 2024-09-24 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0043_rename_description_kz_hotel_description_kk_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomtype',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
