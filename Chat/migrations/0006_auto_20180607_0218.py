# Generated by Django 2.0.4 on 2018-06-06 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0005_auto_20180607_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='image',
            field=models.ImageField(default='../../static/1.jpg', upload_to='Chat/static/images/'),
        ),
    ]
