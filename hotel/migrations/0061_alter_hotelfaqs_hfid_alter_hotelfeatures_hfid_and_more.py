# Generated by Django 4.2.2 on 2024-12-02 21:09

from django.db import migrations, models
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0060_alter_hotelfaqs_hfid_alter_hotelfeatures_hfid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelfaqs',
            name='hfid',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvxyz', length=10, max_length=20, prefix='', unique=True),
        ),
        migrations.AlterField(
            model_name='hotelfeatures',
            name='hfid',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='hotelgallery',
            name='hgid',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='rtid',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvxyz', length=10, max_length=20, prefix='', unique=True),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
