# Generated by Django 2.2.3 on 2019-08-02 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='quesiton',
            new_name='question',
        ),
    ]