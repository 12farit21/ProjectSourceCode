# Generated by Django 4.2.2 on 2024-09-14 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0037_remove_roomtype_images_roomtypeimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomTypeGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='room_type_images/')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='hotel.roomtype')),
            ],
            options={
                'verbose_name_plural': 'RoomType Gallery',
            },
        ),
        migrations.DeleteModel(
            name='RoomTypeImage',
        ),
    ]
