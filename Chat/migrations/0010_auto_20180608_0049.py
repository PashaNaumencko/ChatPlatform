# Generated by Django 2.0.4 on 2018-06-07 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0009_auto_20180608_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='image',
            field=models.ImageField(default='chat_avatar/1.png', upload_to='chat_avatar'),
        ),
    ]