# Generated by Django 3.0.5 on 2020-04-05 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_items_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='category',
            field=models.CharField(choices=[('Sh', 'Shirts'), ('Tr', 'Trousers')], default='Sh', max_length=2),
        ),
    ]
