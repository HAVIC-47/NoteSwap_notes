# Generated by Django 5.1.3 on 2024-11-29 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NoteSwap_main', '0009_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
    ]