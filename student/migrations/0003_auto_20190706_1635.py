# Generated by Django 2.2.2 on 2019-07-06 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20190706_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='display_picture',
            field=models.ImageField(blank=True, null=True, upload_to='user/dp/display_picture/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='user/wall/picture/%Y/%m/%d'),
        ),
    ]
