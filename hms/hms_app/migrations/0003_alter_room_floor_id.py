# Generated by Django 3.2.6 on 2021-11-20 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hms_app', '0002_auto_20211121_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='floor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='floors_id', to='hms_app.room_floor'),
        ),
    ]
