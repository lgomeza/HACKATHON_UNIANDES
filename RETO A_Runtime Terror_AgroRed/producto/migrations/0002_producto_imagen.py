# Generated by Django 2.2.6 on 2019-10-26 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default=' ', upload_to='images/'),
            preserve_default=False,
        ),
    ]
