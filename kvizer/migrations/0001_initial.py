# Generated by Django 2.2.6 on 2020-05-13 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Korisnik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip', models.CharField(choices=[('Učenik', 'Učenik'), ('Profesor', 'Profesor')], max_length=200)),
                ('ime', models.CharField(max_length=200)),
                ('prezime', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('lozinka', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Kviz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=300)),
                ('predmet', models.CharField(choices=[('Matematika', 'Matematika'), ('Fizika', 'Fizika'), ('Srpski jezik i književnost', 'Srpski jezik i književnost'), ('Srpski kao nematernji jezik', 'Srpski kao nematernji'), ('Bosanski jezik i književnost', 'Bosanski jezik i književnost'), ('Engleski jezik', 'Engleski jezik'), ('Nemački jezik', 'Nemački jezik'), ('Francuski jezik', 'Francuski jezik'), ('Latinski jezik', 'Latinski jezik'), ('Istorija', 'Istorija'), ('Geografija', 'Geografija'), ('Biologija', 'Biologija'), ('Hemija', 'Hemija'), ('Računarstvo i informatika', 'Računarstvo i informatika'), ('Muzička kultura', 'Muzička kultura'), ('Likovna kultura', 'Likovna kultura'), ('Fizičko vaspitanje', 'Fizičko vaspitanje'), ('Građansko vaspitanje', 'Građansko vaspitanje'), ('Islamska veronauka', 'Islamska veronauka'), ('Pravoslavna veronauka', 'Pravoslavna veronauka'), ('Jezik medija i kultura', 'Jezik medija i kultura'), ('Primenjene nauke', 'Primenjene nauke'), ('Umetnost i dizajn', 'Umetnost i dizajn'), ('Zdravlje i sport', 'Zdravlje i sport'), ('Psihologija', 'Psihologija'), ('Filozofija', 'Filozofija'), ('Sociologija', 'Sociologija'), ('Ustav i prava građana', 'Ustav i prava građana')], max_length=40)),
                ('godina', models.CharField(choices=[('Prva godina', 'Prva godina'), ('Druga godina', 'Druga godina'), ('Treća godina', 'Treća godina'), ('Četvrta godina', 'Četvrta godina')], max_length=40)),
                ('trajanje_kviza', models.PositiveIntegerField()),
                ('id_korisnika', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kvizer.Korisnik')),
            ],
        ),
        migrations.CreateModel(
            name='Rezultat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bodovi', models.SmallIntegerField()),
                ('id_korisnika', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kvizer.Korisnik')),
                ('id_kviza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kvizer.Kviz')),
            ],
        ),
        migrations.CreateModel(
            name='Pitanje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pitanje', models.TextField(max_length=300)),
                ('id_kviza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kvizer.Kviz')),
            ],
        ),
        migrations.CreateModel(
            name='Odgovor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odgovor', models.TextField(max_length=300)),
                ('tacnost', models.BooleanField()),
                ('id_pitanja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kvizer.Pitanje')),
            ],
        ),
    ]
