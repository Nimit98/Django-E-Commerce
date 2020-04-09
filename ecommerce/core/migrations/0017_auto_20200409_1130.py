# Generated by Django 2.2.10 on 2020-04-09 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20200409_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderplaced',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='orderplaced',
            name='total_price',
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='core.ItemOrder'),
        ),
    ]