# Generated by Django 2.0.1 on 2018-03-04 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0022_remove_poll_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]
