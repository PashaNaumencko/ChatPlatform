# Generated by Django 2.0.4 on 2018-06-07 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0010_auto_20180608_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='image',
            field=models.ImageField(default='1.png', upload_to='chat_avatar'),
        ),
    ]
