# Generated by Django 4.2.11 on 2024-05-17 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_alter_student_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]