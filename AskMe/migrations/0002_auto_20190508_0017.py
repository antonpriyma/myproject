# Generated by Django 2.1.7 on 2019-05-07 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AskMe', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='vote',
            new_name='type_vote',
        ),
    ]
