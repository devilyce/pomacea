# Generated by Django 4.0.3 on 2022-04-13 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inquiryform', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='country',
            new_name='state',
        ),
    ]
