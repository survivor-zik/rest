# Generated by Django 4.2.3 on 2023-07-22 13:45

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0002_alter_user_datejoined_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='datejoined',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2023, 7, 22, 18, 45, 29, 787721)),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(8)]),
        ),
    ]