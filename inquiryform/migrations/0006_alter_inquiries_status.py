# Generated by Django 4.0.3 on 2022-04-17 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inquiryform', '0005_status_alter_inquiries_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiries',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='inquiryform.status'),
        ),
    ]
