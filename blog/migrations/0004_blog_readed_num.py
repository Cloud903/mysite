# Generated by Django 2.0 on 2019-04-25 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190424_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='readed_num',
            field=models.IntegerField(default=0),
        ),
    ]
