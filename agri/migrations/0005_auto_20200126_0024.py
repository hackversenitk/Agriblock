# Generated by Django 3.0.2 on 2020-01-26 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0004_auto_20200126_0011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='category',
            new_name='user_type',
        ),
    ]