# Generated by Django 3.2.9 on 2021-11-01 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidature',
            fields=[
                ('CandidatureId', models.AutoField(primary_key=True, serialize=False)),
                ('UniversityName', models.CharField(max_length=500)),
                ('UniversityYear', models.CharField(max_length=500)),
                ('AcademicBackground', models.CharField(max_length=500)),
                ('Relev1', models.CharField(max_length=500)),
                ('Relev2', models.CharField(max_length=500)),
                ('Status', models.CharField(max_length=500)),
                ('Score', models.CharField(max_length=500)),
            ],
        ),
    ]