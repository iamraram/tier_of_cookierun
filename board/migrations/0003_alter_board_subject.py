# Generated by Django 4.2.7 on 2023-11-10 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_rename_date_board_create_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='subject',
            field=models.CharField(max_length=128),
        ),
    ]
