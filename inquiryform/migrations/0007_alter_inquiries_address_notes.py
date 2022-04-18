# Generated by Django 4.0.3 on 2022-04-18 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inquiryform', '0006_alter_inquiries_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiries',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('inquiries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='inquiryform.inquiries')),
            ],
        ),
    ]