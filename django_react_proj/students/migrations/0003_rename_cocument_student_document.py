# Generated by Django 3.2.7 on 2021-09-21 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_students'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='cocument',
            new_name='document',
        ),
    ]
