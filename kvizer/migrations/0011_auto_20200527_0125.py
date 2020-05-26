# Generated by Django 2.2.6 on 2020-05-27 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvizer', '0010_auto_20200526_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kviz',
            name='godina',
            field=models.CharField(choices=[('Prva godina', 'Prva godina'), ('Druga godina', 'Druga godina'), ('Treća godina', 'Treća godina'), ('Četvrta godina', 'Četvrta godina')], default='1', max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='godina',
            field=models.CharField(blank=True, choices=[('Prva godina', 'Prva godina'), ('Druga godina', 'Druga godina'), ('Treća godina', 'Treća godina'), ('Četvrta godina', 'Četvrta godina')], max_length=40, null=True),
        ),
    ]
