# Generated by Django 3.2.4 on 2021-06-12 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_auto_20210612_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(default='hello@iitg.ac.in', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.CharField(default='0000000000', max_length=100),
        ),
    ]
