# Generated by Django 4.0.3 on 2022-04-11 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(max_length=255, null=True),
        ),
    ]