# Generated by Django 4.2.4 on 2023-09-05 23:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel', '0011_roomtype_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='guest',
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_id',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvxyz', length=10, max_length=20, prefix='', unique=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotel.hotel'),
        ),
        migrations.AddField(
            model_name='booking',
            name='num_adults',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='booking',
            name='num_children',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='roomtype',
            name='room_capacity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='booking',
            name='room',
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='number_of_beds',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='BookingDetail',
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ManyToManyField(to='hotel.room'),
        ),
    ]
