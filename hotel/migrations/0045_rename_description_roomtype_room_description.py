# Generated by Django 4.2.2 on 2024-09-24 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0044_roomtype_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roomtype',
            old_name='description',
            new_name='room_description',
        ),
    ]
