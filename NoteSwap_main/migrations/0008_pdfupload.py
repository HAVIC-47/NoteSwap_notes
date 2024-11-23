# Generated by Django 5.0.7 on 2024-11-18 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NoteSwap_main', '0007_rename_notes_note_rename_users_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDFUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pdf_file', models.FileField(upload_to='pdfs/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
