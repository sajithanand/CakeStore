# Generated by Django 5.0.2 on 2024-03-05 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_cart_quantity_cart_status_occasion_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='zipcode',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]
