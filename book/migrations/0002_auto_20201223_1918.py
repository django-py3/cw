# Generated by Django 3.1.4 on 2020-12-23 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='booktitle',
            new_name='title',
        ),
    ]