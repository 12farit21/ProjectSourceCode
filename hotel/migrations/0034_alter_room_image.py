# Generated by Django 4.2.2 on 2024-09-13 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0033_remove_roomtype_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='room_gallery', verbose_name='Картинка'),
        ),
    ]
