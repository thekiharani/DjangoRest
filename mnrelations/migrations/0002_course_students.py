# Generated by Django 3.0.6 on 2020-05-17 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mnrelations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='mnrelations.Student'),
        ),
    ]
