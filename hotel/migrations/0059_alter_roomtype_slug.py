# Generated by Django 4.2.2 on 2024-12-02 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0058_alter_hotelfeatures_hfid_alter_hotelgallery_hgid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomtype',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
