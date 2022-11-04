# Generated by Django 4.1.3 on 2022-11-03 20:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('iou', '0003_alter_iouuser_options_alter_iouuser_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='ledger',
            name='expiration',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
