# Generated by Django 3.2.6 on 2021-11-22 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms_app', '0005_auto_20211121_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='housekeeper',
            name='housekeeper_mobile',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='room_details',
            name='room_occupancy',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='room_details',
            name='room_status',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='room_details',
            name='room_type',
            field=models.CharField(max_length=20),
        ),
    ]
