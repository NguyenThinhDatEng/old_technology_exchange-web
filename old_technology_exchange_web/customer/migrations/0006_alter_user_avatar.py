# Generated by Django 4.0.3 on 2022-04-11 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_rename_sex_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(default='', max_length=255),
        ),
    ]