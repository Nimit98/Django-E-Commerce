# Generated by Django 3.0.5 on 2020-04-07 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_itemorder_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='category',
            field=models.CharField(choices=[('Sh', 'Shirts'), ('Tr', 'Trousers'), ('Bl', 'Blazzer')], default='Bl', max_length=2),
        ),
    ]
