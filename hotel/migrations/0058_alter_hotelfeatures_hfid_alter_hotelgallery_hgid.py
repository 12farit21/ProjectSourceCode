# Generated by Django 4.2.2 on 2024-12-02 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0057_alter_hotelgallery_hgid'),
    ]

    operations = [
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
    ]
