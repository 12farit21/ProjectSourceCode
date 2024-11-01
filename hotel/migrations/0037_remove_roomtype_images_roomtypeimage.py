# Generated by Django 4.2.2 on 2024-09-13 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0036_roomtype_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomtype',
            name='images',
        ),
        migrations.CreateModel(
            name='RoomTypeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='room_type_images/')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='hotel.roomtype')),
            ],
        ),
    ]
