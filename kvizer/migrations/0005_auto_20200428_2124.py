# Generated by Django 2.2.6 on 2020-04-28 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvizer', '0004_auto_20200423_1735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pitanje',
            old_name='text',
            new_name='pitanje',
        ),
        migrations.AlterField(
            model_name='kviz',
            name='trajanje_kviza',
            field=models.PositiveIntegerField(),
        ),
    ]
