# Generated by Django 4.0.5 on 2022-06-27 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_id', models.IntegerField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('champions', models.CharField(max_length=250)),
            ],
        ),
    ]
