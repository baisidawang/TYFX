# Generated by Django 2.0 on 2024-03-12 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0003_auto_20231214_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]