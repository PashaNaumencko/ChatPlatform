# Generated by Django 2.0.4 on 2018-06-06 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0004_auto_20180607_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='image',
            field=models.ImageField(default='../../static/1.jpg', upload_to='static/images/'),
        ),
    ]
