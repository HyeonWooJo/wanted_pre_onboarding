# Generated by Django 4.1 on 2022-08-15 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comapny_name', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'postings',
            },
        ),
    ]
