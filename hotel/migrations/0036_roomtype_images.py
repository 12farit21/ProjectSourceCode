# Generated by Django 4.2.2 on 2024-09-13 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0035_alter_room_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomtype',
            name='images',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
