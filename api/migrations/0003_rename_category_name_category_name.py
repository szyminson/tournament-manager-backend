# Generated by Django 4.0.4 on 2022-05-05 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_tournament_date_remove_tournament_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='name',
        ),
    ]
