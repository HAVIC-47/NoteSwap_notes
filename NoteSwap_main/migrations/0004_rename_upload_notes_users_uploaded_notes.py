# Generated by Django 5.0.7 on 2024-11-07 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NoteSwap_main', '0003_rename_user_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='upload_notes',
            new_name='uploaded_notes',
        ),
    ]
