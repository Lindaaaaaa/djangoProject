# Generated by Django 2.0.2 on 2018-02-19 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='threat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('filename', models.CharField(max_length=100)),
                ('action', models.CharField(max_length=100)),
                ('submit_type', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=100)),
            ],
        ),
    ]
