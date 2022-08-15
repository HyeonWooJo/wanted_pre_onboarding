# Generated by Django 4.1 on 2022-08-15 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posting',
            old_name='comapny_name',
            new_name='position',
        ),
        migrations.RenameField(
            model_name='posting',
            old_name='country',
            new_name='stack',
        ),
        migrations.RemoveField(
            model_name='posting',
            name='location',
        ),
        migrations.AddField(
            model_name='posting',
            name='content',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='posting',
            name='reward',
            field=models.IntegerField(default=0),
        ),
    ]
