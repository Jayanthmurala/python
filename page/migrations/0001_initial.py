# Generated by Django 5.1.3 on 2024-11-17 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='To_do_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=255)),
                ('task_details', models.TextField()),
                ('target_time', models.DateTimeField()),
                ('uploded_on', models.DateTimeField(auto_now=True)),
                ('upgrade_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
