# Generated by Django 2.1.7 on 2019-04-13 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AskMe', '0003_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='text',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
