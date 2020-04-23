# Generated by Django 2.2.6 on 2020-04-23 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kvizer', '0002_auto_20200423_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kviz',
            name='naziv',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='kviz',
            name='trajanje_kviza',
            field=models.PositiveIntegerField(help_text='Trajanje kviza je u minutama'),
        ),
        migrations.CreateModel(
            name='Pitanje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('id_kviza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kvizer.Kviz')),
            ],
        ),
        migrations.CreateModel(
            name='Odgovor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tacnost', models.BooleanField()),
                ('id_pitanja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kvizer.Pitanje')),
            ],
        ),
    ]
