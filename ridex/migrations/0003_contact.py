# Generated by Django 4.0.6 on 2023-06-29 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ridex', '0002_payment_delete_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('mail', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
        ),
    ]