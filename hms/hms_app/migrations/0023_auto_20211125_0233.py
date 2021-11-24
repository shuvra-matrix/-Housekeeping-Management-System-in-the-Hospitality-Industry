# Generated by Django 3.2.6 on 2021-11-24 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hms_app', '0022_auto_20211125_0158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room_service',
            name='food_quentity',
        ),
        migrations.RemoveField(
            model_name='room_service',
            name='food_type',
        ),
        migrations.RemoveField(
            model_name='room_service',
            name='room_scervice_updated_by',
        ),
        migrations.AddField(
            model_name='food_order_list',
            name='show_list',
            field=models.CharField(default='yes', max_length=5),
        ),
        migrations.AddField(
            model_name='room_service',
            name='food_list_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='hms_app.food_order_list'),
            preserve_default=False,
        ),
    ]
