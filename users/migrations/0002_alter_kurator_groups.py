# Generated by Django 4.2.11 on 2024-05-17 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_group_department'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kurator',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='kurator_assigned', to='groups.group'),
        ),
    ]