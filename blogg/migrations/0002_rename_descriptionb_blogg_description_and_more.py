# Generated by Django 4.1.2 on 2022-10-12 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogg', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogg',
            old_name='descriptionb',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='blogg',
            old_name='titleb',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='blogg',
            old_name='urlb',
            new_name='url',
        ),
    ]
